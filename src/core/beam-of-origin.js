'use strict';
// Measured viewport polygons only. No placement decisions, HA state or actions.
function settings(value) {
    if(value===undefined || value===false)return null;
    const options=value===true?{}:value;
    if(!options || typeof options!=='object' || Array.isArray(options) || Object.keys(options).some(k=>k!=='color'))
        throw Error('collapsible.beam_of_origin must be true, false or {color: CSS color}.');
    const color=options.color===undefined?'#8bdcff':options.color;
    // Use the same CSS-color contract in Node and the browser. No paint servers,
    // template expressions or inherited values that can change the beam's hue.
    const valid=typeof color==='string' && /^(#[\da-f]{3,4}|#[\da-f]{6}|#[\da-f]{8}|(?:rgb|hsl)a?\([\d\s.,%+\/-]+\)|[a-z]+)$/i.test(color.trim()) &&
        !/^(inherit|initial|unset|revert|currentcolor)$/i.test(color.trim());
    if(!valid || typeof CSS!=='undefined' && !CSS.supports('color',color))throw Error('Invalid collapsible.beam_of_origin.color.');
    return {color};
}
function hex(rect) {
    return [[.5,0],[1,.25],[1,.75],[.5,1],[0,.75],[0,.25]].map(([x,y])=>({x:rect.left+x*rect.width,y:rect.top+y*rect.height}));
}
const center=p=>({x:p.reduce((s,v)=>s+v.x,0)/p.length,y:p.reduce((s,v)=>s+v.y,0)/p.length});
const cross=(a,b)=>a.x*b.y-a.y*b.x;
const sub=(a,b)=>({x:a.x-b.x,y:a.y-b.y});
const distance=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
// Separating axes preserve the real hex corners (AABB overlap is insufficient).
function overlaps(a,b) {
    return [...a,...b].every((v,i,all)=>{
        const poly=i<a.length?a:b,j=i<a.length?i:i-a.length,w=poly[(j+1)%poly.length],axis={x:-(w.y-v.y),y:w.x-v.x};
        const project=p=>p.map(q=>q.x*axis.x+q.y*axis.y),aa=project(a),bb=project(b);
        return Math.max(...aa)>=Math.min(...bb) && Math.max(...bb)>=Math.min(...aa);
    });
}
// Find the facing perimeter intersection, then walk along its two sides. Every
// end of the fan lies on a physical outer hex boundary, in any direction.
function cap(poly,toward,width) {
    const c=center(poly),d=sub(toward,c);
    for(let i=0;i<poly.length;i++) {
        const a=poly[i],b=poly[(i+1)%poly.length],edge=sub(b,a),den=cross(d,edge);
        if(Math.abs(den)<1e-8)continue;
        const t=cross(sub(a,c),edge)/den,u=cross(sub(a,c),d)/den;
        if(t<0 || u<0 || u>1)continue;
        const hit={x:c.x+d.x*t,y:c.y+d.y*t};
        const walk=direction=>{
            let point=hit,index=direction>0?(i+1)%poly.length:i,remaining=width;
            for(let step=0;step<poly.length;step++) {
                const end=poly[index],length=distance(point,end);
                if(remaining<=length)return {x:point.x+(end.x-point.x)*remaining/length,y:point.y+(end.y-point.y)*remaining/length};
                remaining-=length;point=end;index=(index+direction+poly.length)%poly.length;
            }
            return point;
        };
        return {center:hit,ends:[walk(-1),walk(1)]};
    }
    return null;
}
function hull(points) {
    const sorted=[...points].sort((a,b)=>a.x-b.x || a.y-b.y),half=values=>{
        const result=[];
        for(const p of values){while(result.length>1 && cross(sub(result[result.length-1],result[result.length-2]),sub(p,result[result.length-1]))<=0)result.pop();result.push(p);}
        return result;
    };
    const lower=half(sorted),upper=half([...sorted].reverse());lower.pop();upper.pop();return lower.concat(upper);
}
function nearestBoundary(point,targets) {
    let best=null,bestDistance=Infinity;
    for(const poly of targets)for(let i=0;i<poly.length;i++){
        const a=poly[i],b=poly[(i+1)%poly.length],edge=sub(b,a),offset=sub(point,a);
        const t=Math.max(0,Math.min(1,(offset.x*edge.x+offset.y*edge.y)/(edge.x*edge.x+edge.y*edge.y)));
        const p={x:a.x+t*edge.x,y:a.y+t*edge.y},d=distance(point,p);
        if(d<bestDistance){best=p;bestDistance=d;}
    }
    return best;
}
function connection(source,targets) {
    const origin=hex(source);
    if(!targets.length)return null;
    const outline=hull(targets.flat()),c=center(origin),destination=center(outline);
    if(overlaps(origin,outline))return null;
    // Suppress short/ambiguous links using the nearest real physical boundary.
    const gaps=targets.map(target=>{
        const s=cap(origin,center(target),0),t=cap(target,c,0);
        return s&&t?distance(s.center,t.center):Infinity;
    });
    if(Math.min(...gaps)<Math.max(8,source.width*.12))return null;
    const axis=sub(destination,c),length=Math.hypot(axis.x,axis.y);
    if(!length)return null;
    const side=p=>cross(axis,sub(p,c))/length,projections=outline.map(side);
    const s=cap(origin,destination,source.width*.32),t=cap(outline,c,(Math.max(...projections)-Math.min(...projections))*.45);
    if(!s || !t)return null;
    // A convex outline can bridge gaps between cubes. Attach each fan corner
    // back to an actual rendered hex, never to empty scene/container padding.
    t.ends=t.ends.map(point=>nearestBoundary(point,targets));
    t.center=nearestBoundary(t.center,targets);
    s.ends.sort((a,b)=>side(a)-side(b));t.ends.sort((a,b)=>side(a)-side(b));
    return {source:s.center,target:t.center,points:[s.ends[0],s.ends[1],t.ends[1],t.ends[0]]};
}
module.exports={settings,hex,overlaps,connection};
