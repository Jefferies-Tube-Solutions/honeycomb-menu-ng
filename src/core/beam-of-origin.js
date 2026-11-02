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
function connection(source,targets) {
    const origin=hex(source);
    if(!targets.length || targets.some(p=>overlaps(origin,p)))return null;
    const c=center(origin);
    // Choose the nearest facing physical control, not a container's empty space.
    const candidates=targets.map(target=>{
        const tc=center(target),s=cap(origin,tc,source.width*.22),t=cap(target,c,distance(target[0],target[3])*.28);
        return s&&t?{s,t,gap:distance(s.center,t.center)}:null;
    }).filter(Boolean).sort((a,b)=>a.gap-b.gap);
    const best=candidates[0];
    if(!best || best.gap<Math.max(8,source.width*.12))return null;
    const {s,t}=best;
    const axis=sub(t.center,s.center),side=p=>cross(axis,sub(p,s.center));
    s.ends.sort((a,b)=>side(a)-side(b));t.ends.sort((a,b)=>side(a)-side(b));
    return {source:s.center,target:t.center,points:[s.ends[0],s.ends[1],t.ends[1],t.ends[0]]};
}
module.exports={settings,hex,overlaps,connection};
