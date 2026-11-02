"""Static site structure, guide coverage and contrast checks; no browser required."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.assets, self.options = [], [], [], []
        self.hidden = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        if tag == 'option' and a.get('value'):
            self.options.append(a['value'])
        if tag in ('script','img') and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'link' and a.get('href'):
            self.assets.append(a['href'])
        if 'hidden' in a:
            self.hidden.append(a.get('id'))
    def handle_data(self, text):
        self.text.append(text)

class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page=Page()
        cls.page.feed((ROOT/'index.html').read_text())
        cls.catalog=json.loads((ROOT/'programs.json').read_text())
    def test_all_programs_are_present(self):
        self.assertEqual(len(self.catalog),61)
        for item in self.catalog:
            self.assertIn('program-'+item['slug'],self.page.ids)
            self.assertIn('program-'+item['slug'],self.page.options)
            self.assertTrue((ROOT/item['path']).is_file())
    def test_original_order(self):
        order=[x for x in self.page.ids if x.startswith('program-') and x != 'program-jump']
        self.assertEqual(order,['program-'+x['slug'] for x in self.catalog])
        self.assertLess(order.index('program-routersploit'),order.index('program-nmap'))
        self.assertLess(order.index('program-hydra'),order.index('program-sqlmap'))
    def test_internal_anchors(self):
        missing=[x for x in self.page.links if x.startswith('#') and x[1:] not in self.page.ids]
        self.assertEqual(missing,[])
    def test_ids_are_unique(self):
        self.assertEqual([x for x,n in Counter(self.page.ids).items() if n>1],[])
    def test_runtime_assets_are_local(self):
        for asset in self.page.assets:
            self.assertFalse(asset.startswith(('http:','https:','//')))
            self.assertTrue((ROOT/asset).is_file(),asset)
    def test_no_hidden_tool_content(self):
        self.assertEqual(self.page.hidden,['status'])
        script=(ROOT/'assets/app.js').read_text()
        self.assertNotIn('.guide',script)
        self.assertNotIn('innerHTML',script)
    def test_required_guide_sections(self):
        for item in self.catalog:
            text=(ROOT/item['path']).read_text()
            for section in ('## Install and verify','## Use it in practice','**Troubleshooting:**','**Cleanup:**'):
                self.assertIn(section,text,item['slug'])
    def test_text_contrast(self):
        def lum(hexcolor):
            channels=[int(hexcolor[i:i+2],16)/255 for i in (0,2,4)]
            v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in channels]
            return sum(a*b for a,b in zip(v,(.2126,.7152,.0722)))
        for fg in ('edf0f2','b8bdc5','d5e3db'):
            for bg in ('111214','1a1b1e'):
                ratio=(max(lum(fg),lum(bg))+.05)/(min(lum(fg),lum(bg))+.05)
                self.assertGreaterEqual(ratio,4.5)

if __name__=='__main__':
    unittest.main()
