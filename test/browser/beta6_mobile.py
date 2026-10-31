"""Mobile free-canvas follow-up. Browser plugin not available; local Chromium.
Flow: hold compact floorplan Hub -> free external canvas -> submenu/Back/collapse.
Synthetic HA only. Published beta.6 remains immutable; this test never releases.
"""
import argparse,json,os,shutil,subprocess,threading,unittest
from pathlib import Path
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from run import Handler,CheckResult
from beta6_placement import Placement

class Mobile(Placement):
 def floor(self,*args,**kwargs):
  kwargs['items']=[{'type':'light','entity':'light.zone_a','slot':0},{'type':'light','entity':'light.zone_a','slot':2},{**self.sonos_item(),'slot':3},{'type':'generic','entity':'sensor.value_a','slot':1,'icon':'mdi:circle'}]
  return super().floor(*args,**kwargs)
 def diagnostics(self):
  s=self.state();s['origin']=self.origin();s['boxes']=self.boxes()
  s['actual']=self.page.evaluate("()=>{const m=hub._hubMenu,c=m._computeCenterPosition(),cx=c.x+.5,cy=c.y+1.1547/2,ps=[c];m.buttons.forEach((b,i)=>{if(b!==undefined){const p=m._computeButtonPosition(i);if(p)ps.push(p)}});return {left:Math.min(...ps.map(p=>p.x-cx)),right:Math.max(...ps.map(p=>p.x+1-cx)),top:Math.min(...ps.map(p=>p.y-cy)),bottom:Math.max(...ps.map(p=>p.y+1.1547-cy))}}")
  s.update(json.loads(subprocess.check_output(['node','-e',"const g=require('./src/core/expanded-layout'),s=JSON.parse(process.argv[1]),v=s.environment.viewport,p=g.workingFootprint(s.actual);console.log(JSON.stringify({planning:p,smallScreen:g.smallScreen(s.actual,v,100),regions:g.freeRegions(v,s.image).map(region=>({region,actualMax:g.fittedSize(s.actual,region,100),planningMax:g.fittedSize(p,region,100),rejection:g.fittedSize(p,region,100)<85?'planning envelope below 85%':null}))}))",json.dumps(s)],text=True)))
  return s
 def save(self,name):
  (self.evidence/f'{self.viewport["width"]}-{name}.json').write_text(json.dumps(self.diagnostics(),indent=2));self.capture(name)
 def test_upper_image_external_canvas_and_exact_Back(self):
  self.setup_image(min(330,self.viewport['height']*.35));before=self.box();self.capture('collapsed');self.expand();self.page.wait_for_timeout(550);s=self.diagnostics();self.assertAlmostEqual(s['size'],100,delta=.05);self.assertEqual(self.controls().count(),4);self.assert_fit();self.save('expanded')
  if self.before and s['smallScreen']:self.assertEqual(s['root']['region']['key'],'viewport')
  else:self.assertEqual(s['root']['region']['key'],'below');self.assert_fit(s['root']['region']);self.assertGreaterEqual(min(b['y'] for b in s['boxes']),s['image']['bottom']+12-.2)
  parent=self.boxes();selected=self.cell(3).bounding_box();self.hold_input(self.cell(3).locator('.interaction-surface'));self.settle();self.assertGreater(self.page.evaluate('hub._menuContext.stack.length'),0);self.assert_fit()
  if self.state()['fit']['reason']=='selected':self.assert_same(selected,self.box())
  self.back();self.settle()
  for a,b in zip(parent,self.boxes()):self.assert_same(a,b)
  self.back();self.settle();self.assert_same(before,self.box());self.assertEqual(self.page.evaluate('calls.length'),0);self.capture('restored')
 def test_desktop_short_wide_and_constrained_images(self):
  for width,height in [(1440,900),(1920,1080),(2560,1440),(3440,1440)]:
   self.page.set_viewport_size({'width':width,'height':height});self.viewport={'width':width,'height':height}
   for name,bottom in [('roomy',min(360,height*.3)),('strip',height-180)]:
    self.setup_image(bottom);before=self.box();self.expand();self.page.wait_for_timeout(550);s=self.diagnostics();self.assertAlmostEqual(s['size'],100,delta=.05);self.assert_fit();self.assertFalse(s['smallScreen'])
    if name=='roomy':self.assertEqual(s['root']['region']['key'],'below');self.assert_fit(s['root']['region']);self.assertGreaterEqual(next(r['planningMax'] for r in s['regions'] if r['region']['key']=='below'),100-.001)
    else:self.assertEqual(s['root']['region']['key'],'viewport');self.assertEqual(s['anchor'],s['origin'])
    self.save(name);self.back();self.settle();self.assert_same(before,self.box());self.reset()
 def test_constrained_panel_safe_insets_scroll_and_rotation(self):
  self.setup_image(300);self.page.evaluate("()=>{const sidebar=document.createElement('ha-sidebar');sidebar.style.cssText='position:fixed;left:0;top:0;width:600px;height:100vh';document.body.append(sidebar);hub._hubMenu.style.setProperty('--hub-safe-bottom','20px');const right=document.createElement('ha-sidebar');right.style.cssText='position:fixed;right:0;top:0;width:440px;height:100vh';document.body.append(right);window.testSidebar=[sidebar,right];hub.style.left='55.5%'}")
  self.page.wait_for_timeout(150);self.settle();self.expand();self.page.wait_for_timeout(550);self.assert_fit();self.assertEqual(self.state()['root']['region']['key'],'below');self.assert_fit(self.state()['root']['region']);self.save('constrained-panel')
  self.page.evaluate('testSidebar.forEach(el=>el.remove())');self.back();self.settle();self.reset()
  self.viewport={'width':390,'height':844};self.page.set_viewport_size(self.viewport);self.setup_image(300);self.expand();self.page.wait_for_timeout(550)
  for width,height in [(844,390),(430,932),(390,844)]:
   self.page.set_viewport_size({'width':width,'height':height});self.page.evaluate("([w,h])=>{floor.style.width=w+'px';floor.style.height=Math.min(300,h*.35)+'px';imageHost.style.height=floor.style.height;floor.style.transform='translateY(-10px)';floorImage.style.objectPosition='right bottom'}",[width,height]);self.page.wait_for_timeout(150);self.settle();self.assertEqual(self.state()['root']['region']['key'],'below');self.assert_fit(self.state()['root']['region'])
  self.back();self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'));self.assertAlmostEqual(self.box()['width'],self.page.evaluate('hub.size'),delta=.15)

def main():
 p=argparse.ArgumentParser();p.add_argument('--bundle',type=Path,required=True);p.add_argument('--button-card',type=Path,required=True);p.add_argument('--floorplan',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--before',action='store_true');a=p.parse_args();a.evidence_dir.mkdir(parents=True,exist_ok=True)
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);server.bundle=a.bundle.resolve();server.button=a.button_card.resolve();threading.Thread(target=server.serve_forever,daemon=True).start();success=True
 try:
  with sync_playwright() as pw:
   Mobile.browser=pw.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox']);Mobile.url=f'http://127.0.0.1:{server.server_port}';Mobile.evidence=a.evidence_dir;Mobile.floorplan=a.floorplan.resolve();Mobile.before=a.before
   for width,height in [(390,844),(430,932),(844,390),(800,1280)]:
    Mobile.viewport={'width':width,'height':height};names=['test_upper_image_external_canvas_and_exact_Back'];r=unittest.TextTestRunner(verbosity=2,resultclass=CheckResult).run(unittest.TestSuite(Mobile(n) for n in names));success=r.wasSuccessful() and success
   Mobile.viewport={'width':1440,'height':900};r=unittest.TextTestRunner(verbosity=2,resultclass=CheckResult).run(unittest.TestSuite(Mobile(n) for n in ['test_desktop_short_wide_and_constrained_images']+([] if a.before else ['test_constrained_panel_safe_insets_scroll_and_rotation'])));success=r.wasSuccessful() and success
   Mobile.browser.close()
 finally:server.shutdown();server.server_close()
 return 0 if success else 1
if __name__=='__main__':raise SystemExit(main())
