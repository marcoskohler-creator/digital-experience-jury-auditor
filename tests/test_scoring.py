import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import unittest
from engine.scoring import awwwards, webby, cssda, digital_excellence

class ScoringTests(unittest.TestCase):
    def test_awwwards_formula(self):
        r=awwwards({"design":8,"usability":7,"creativity":9,"content":6})
        self.assertAlmostEqual(r.score,7.7,places=3)
        self.assertEqual(r.status,"VERIFIED")
    def test_no_evidence_no_score(self):
        r=awwwards({"design":8,"usability":None,"creativity":None,"content":None})
        self.assertIsNone(r.score)
        self.assertEqual(r.status,"NOT_VERIFIED")
    def test_webby_is_internal_partial_not_fake_official(self):
        vals={"content":8,"structure_and_navigation":8,"visual_design":8,"functionality":8,"interactivity":8,"innovation":None,"overall_experience":8}
        r=webby(vals)
        self.assertEqual(r.status,"VERIFIED_PARTIAL")
        self.assertAlmostEqual(r.score,8.0)
    def test_cssda_requires_two_dimensions(self):
        r=cssda({"ui":9,"ux":None,"innovation":None})
        self.assertIsNone(r.score)
    def test_des_cap(self):
        vals={k:95 for k in ["experience_craft","ux_usability","engineering_performance","seo_discoverability","accessibility","content","conversion","resilience_security_privacy"]}
        self.assertEqual(digital_excellence(vals,caps=[70]).score,70)

if __name__=='__main__': unittest.main()
