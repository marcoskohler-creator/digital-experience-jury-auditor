import sys, json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import unittest
from engine.confidence import confidence, band
from engine.regression import compare
from engine.calibration import sanity_check

class OtherTests(unittest.TestCase):
    def test_confidence(self):
        c=confidence(1,1,1,1); self.assertEqual(c,100); self.assertEqual(band(c),"VERY_HIGH")
    def test_regression(self):
        self.assertEqual(compare(80,76)["status"],"REGRESSED")
        self.assertEqual(compare(80,90,methodology_compatible=False)["status"],"NOT_COMPARABLE")
    def test_calibration_fixture(self):
        p=Path(__file__).resolve().parents[1]/"benchmarks/fixtures/calibration.synthetic.json"
        rows=json.loads(p.read_text())
        r=sanity_check([x["score"] for x in rows],[x["label"] for x in rows])
        self.assertEqual(r["status"],"PASS")

if __name__=='__main__': unittest.main()
