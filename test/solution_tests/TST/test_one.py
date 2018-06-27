import unittest

from solutions.TST import one
from solutions.CHK import checkout_solution

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(one.get(), 1)


class TestCHK(unittest.TestCase):
    def test_chk_multipleA_1(self):
        self.assertEqual(checkout_solution.checkout("AAA"), 130)

    def test_chk_multipleAB1(self):
        self.assertEqual(checkout_solution.checkout("ABABA"), 175)

    def test_chk_multipleAB2(self):
        self.assertEqual(checkout_solution.checkout("ABBBBAA"), 220)

    def test_chk_multipleAB_and_C(self):
        self.assertEqual(checkout_solution.checkout("ABBBBAACCC"), 220)

    def test_chk_multipleCD(self):
        self.assertEqual(checkout_solution.checkout("CD"), 220)

    def test_chk_empty_string(self):
        self.assertEqual(checkout_solution.checkout(""), 220)

    def test_chk_string_invalid_products(self):
        self.assertEqual(checkout_solution.checkout("EFG"), 220)

    def test_chk_multipleAB_and_C(self):
        self.assertEqual(checkout_solution.checkout("ABBBBAACCC"), 220)

if __name__ == '__main__':
    unittest.main()
