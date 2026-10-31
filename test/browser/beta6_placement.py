"""Issue #148 beta.6 geometry; Browser plugin not available, repository Playwright.
Synthetic HA services and pinned public HA floorplan, never real device acceptance.
"""
import argparse,json,os,shutil,threading,unittest,hashlib
from pathlib import Path
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from run import Handler,CheckResult
from beta5_geometry import Geometry

class Placement(Geometry):
 def setup_image(self,bottom):
  self.floor('full',items=[{'type':'light','entity':'light.zone_a','slot':0},{'type':'light','entity':'light.zone_b','slot':2},{'type':'generic','entity':'sensor.value_a','icon':'mdi:circle','slot':1},{'type':'generic','entity':'sensor.value_a','icon':'mdi:circle','slot':3}])
  self.page.route('**/floorplan.png',lambda route:route.fulfill(path=str(self.floorplan),content_type='image/png'))
  self.page.evaluate("async bottom=>{floor.style.cssText=`position:fixed;left:0;top:0;width:${innerWidth}px;height:${bottom}px;margin:0`;imageHost.style.height=bottom+'px';floorImage.src='/floorplan.png';await floorImage.decode()}",bottom)
  self.page.wait_for_timeout(150);self.settle()
 def origin(self):return self.page.evaluate('()=>{const r=hub.getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2}}')
 def record(self,name):
  state=self.state();state['boxes']=self.boxes();state['origin']=self.origin()
  (self.evidence/f'{self.viewport["width"]}-{name}.json').write_text(json.dumps(state,indent=2));self.capture(name)
 def test_owner_scenarios_A_and_B(self):
  for name,bottom in [('A-roomy',480),('B-cramped',880)]:
   self.setup_image(bottom);before=self.box();self.capture(name+'-collapsed');origin=self.origin();self.expand();self.page.wait_for_timeout(550);s=self.state();self.assertEqual(self.controls().count(),4);self.assert_fit();self.record(name)
   if self.baseline:
    self.assertEqual(s['root']['region']['key'],'below')
    self.assertGreaterEqual(s['size'],80)
    if name.startswith('B'):self.assertLess(s['size'],100)
   else:
    self.assertAlmostEqual(s['size'],100,delta=.05)
    if name.startswith('A'):
     self.assertEqual(s['root']['region']['key'],'below');self.assert_fit(s['root']['region']);self.assertAlmostEqual(s['anchor']['x'],720,delta=.1)
    else:
     self.assertEqual(s['root']['region']['key'],'viewport');self.assertEqual(s['anchor'],origin)
   self.back();self.settle();self.assert_same(before,self.box());self.reset()
 def test_threshold_sequence_and_original_anchor_after_timeout(self):
  self.page.clock.install();self.setup_image(480);self.expand();self.page.clock.run_for(550);prior_free=True
  # Shared physical hex coordinates span 4.6097 cube widths vertically.
  for scale in [1,.99,.85,.849,.845,.84,.839,.84,.845,.849,.85,1]:
   bottom=self.viewport['height']-16-12-460.97*scale
   self.page.evaluate("b=>{floor.style.height=b+'px';imageHost.style.height=b+'px'}",bottom);self.page.clock.run_for(200);self.settle();s=self.state()
   free=scale>=.85 or scale>=.84 and prior_free
   self.assertEqual(s['root']['region']['key'],'below' if free else 'viewport',str(scale));self.assertAlmostEqual(s['size'],scale*100 if free else 100,delta=.02);self.assert_fit();self.assertEqual(self.controls().count(),4)
   if not free:self.assertEqual(s['anchor'],self.origin())
   self.record('threshold-'+str(scale));prior_free=free
  self.page.clock.run_for(30100);self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'));self.assertEqual(self.controls().count(),1);self.assertAlmostEqual(self.box()['width'],self.page.evaluate('hub.size'),delta=.15);self.capture('timeout-restored')
 def test_responsive_extended_slots_and_nested_exact_Back(self):
  self.floor('full',items=[{'type':'light','entity':'light.zone_a','slot':0},{**self.sonos_item(),'slot':3},{'type':'generic','entity':'sensor.value_a','icon':'mdi:circle','slot':24,'tap_action':{'action':'none'}}]);self.expand();self.page.wait_for_timeout(550);self.assertEqual(self.controls().count(),3);self.assert_fit();parent=self.boxes()
  self.hold_input(self.cell(3).locator('.interaction-surface'));self.settle();self.assert_fit();self.assertGreater(self.page.evaluate('hub._menuContext.stack.length'),0);self.back();self.settle()
  for a,b in zip(parent,self.boxes()):self.assert_same(a,b)
  for width,height in [(390,844),(800,1280),(1440,900),(844,390)]:
   self.page.set_viewport_size({'width':width,'height':height});self.page.evaluate("floor.style.width=innerWidth+'px';floor.style.height=innerHeight+'px';imageHost.style.height=innerHeight+'px'");self.page.wait_for_timeout(180);self.settle();self.assert_fit();self.assertEqual(self.controls().count(),3)
   self.hold_input(self.cell(3).locator('.interaction-surface'));self.settle();child=self.boxes();self.assert_fit();self.back();self.settle();self.assert_fit();self.assertEqual(self.controls().count(),3)
  self.back();self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'));self.assertEqual(self.page.evaluate('calls.length'),0)

def main():
 p=argparse.ArgumentParser();p.add_argument('--bundle',type=Path,required=True);p.add_argument('--button-card',type=Path,required=True);p.add_argument('--floorplan',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--baseline',action='store_true');a=p.parse_args();a.evidence_dir.mkdir(parents=True,exist_ok=True)
 assert hashlib.sha256(a.floorplan.read_bytes()).hexdigest()=='25187fe9fdc4f9d15f28f9f57c4c26a7525c1f979f72eff689d26b0596c449ad'
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);server.bundle=a.bundle.resolve();server.button=a.button_card.resolve();threading.Thread(target=server.serve_forever,daemon=True).start();success=True
 try:
  with sync_playwright() as pw:
   Placement.browser=pw.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox']);Placement.url=f'http://127.0.0.1:{server.server_port}';Placement.evidence=a.evidence_dir;Placement.floorplan=a.floorplan.resolve();Placement.baseline=a.baseline
   for width,height in [(1440,1080)]+([] if a.baseline else [(390,844),(800,1280)]):
    Placement.viewport={'width':width,'height':height};names=['test_owner_scenarios_A_and_B'] if a.baseline else (['test_owner_scenarios_A_and_B','test_threshold_sequence_and_original_anchor_after_timeout'] if width==1440 else [])+['test_responsive_extended_slots_and_nested_exact_Back'];r=unittest.TextTestRunner(verbosity=2,resultclass=CheckResult).run(unittest.TestSuite(Placement(n) for n in names));success=r.wasSuccessful() and success
   Placement.browser.close()
 finally:server.shutdown();server.server_close()
 return 0 if success else 1
if __name__=='__main__':raise SystemExit(main())
