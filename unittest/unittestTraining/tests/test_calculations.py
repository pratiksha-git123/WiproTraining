import unittest

from src.calculations import add, sub, mul, div

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(n1=10, n2=5)
        self.assertEqual(res,  15, "addition Err")

    def test_sub(self):
        res = sub(n1=10, n2=5)
        self.assertEqual(res, 5, "subtraction Err")

    def test_mul(self):
        res = mul(n1=10, n2=5)
        self.assertEqual(res, 50, "multiplication Err")

    def test_div(self):
        res = div(n1=10, n2=5)
        self.assertEqual(res, 2.0, "Division Err")

    def test_ne(self):
        res = (10 != 5)
        self.assertTrue(res, 'NE')
