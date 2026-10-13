import unittest,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from intelligence import analyze_signal,analyze_all
class TestIntelligence(unittest.TestCase):
 def setUp(self):
  self.signals=json.loads((ROOT/'fixtures/signals.json').read_text());self.tenant=json.loads((ROOT/'fixtures/tenant.json').read_text())
 def test_categories(self):
  result=analyze_all(self.signals,self.tenant);self.assertEqual(len(result),4);self.assertIn('online scheduling',result[0]['overlap'])
 def test_augmentations_are_distinct(self):self.assertIn('AI triage',analyze_signal(self.signals[0],self.tenant)['augmentations'])
 def test_invalid_url(self):
  s=dict(self.signals[0]);s['source_url']='localfile';self.assertRaises(ValueError,analyze_signal,s,self.tenant)
 def test_missing_fields(self):self.assertRaises(ValueError,analyze_signal,{},self.tenant)
if __name__=='__main__':unittest.main()
