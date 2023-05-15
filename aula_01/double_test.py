#não consegui rodar os testes em casa :(
import unittest
from math_samples import MathSamples
#python -m unittest ./double_test.py

class DoubleTest(unittest.TestCase):
    def test_double01(self):
        self.assertEqual(
            MathSamples.double(1),
            1)
    
    def test_double01(self):
        self.assertEqual(
        MathSamples.double(2),
        2)

    def test_double01(self):
        self.assertEqual(
        MathSamples.double(3),
        3)