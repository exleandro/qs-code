import unittest
from math_samples import MathSamples

class FibonacciTest(unittest.TestCase):#testcase para teste automatizado

    def teste_fib01(self):
        """Testando caso p/ entrada = 0"""
        self.assertEqual(
            MathSamples.fibonacci(0), #cd teste // python -m unittest ./fibonacci_test.py
            0
        )
    def teste_fib02(self):
        """Testando caso p/ entrada = 1"""
        self.assertEqual(
            MathSamples.fibonacci(1), 
            1
        )
    def teste_fib03(self):
        """Testando caso p/ entrada = 2"""
        self.assertEqual(
            MathSamples.fibonacci(2), 
            1
        )
    def teste_fib04(self):
        """Testando caso p/ entrada = 3"""
        self.assertEqual(
            MathSamples.fibonacci(3), 
            2
        )
    def teste_fib05(self):
        """Testando caso p/ entrada = 4"""#python -m unittest ./fibonacci_test.py
        self.assertEqual(
            MathSamples.fibonacci(4), 
            3
        )
    def teste_fib06(self):
        """Testando caso p/ entrada = 5"""#python -m unittest ./fibonacci_test.py
        self.assertEqual(
            MathSamples.fibonacci(5), 
            5
        )
    def teste_fib07(self):
        """Testando caso p/ entrada = 6"""#python -m unittest ./fibonacci_test.py
        self.assertEqual(
            MathSamples.fibonacci(6), 
            8
        )