import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import unittest
from engine.benchmark import distribution, frequency, classify_sample_size
from engine.patterns import classify_pattern

class BenchmarkTests(unittest.TestCase):
    def test_distribution(self):
        d=distribution([1,2,3,4,5])
        self.assertEqual(d["p50"],3)
        self.assertEqual(d["n"],5)
    def test_sample_warning(self):
        self.assertEqual(classify_sample_size(8,"FULL"),"LOW_SAMPLE_SIZE")
    def test_optional_or_not_correlated(self):
        self.assertEqual(classify_pattern(frequency=.2,correlation_known=False),"NOT_CORRELATED")
    def test_required_beats_frequency(self):
        self.assertEqual(classify_pattern(normative=True,frequency=.01),"REQUIRED")

if __name__=='__main__': unittest.main()
