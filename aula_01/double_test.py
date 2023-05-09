import unittest
from math_samples import MathSamples
#python -m unittest ./double_test.py

class DoubleTest(unittest.TestCase):
    def test_double01(self):
        self.assertEqual(
            MathSamples.double(1),
            1)