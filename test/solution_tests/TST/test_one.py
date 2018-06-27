import unittest

from solutions.TST import one
from solutions.CHK import checkout_solution

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(one.get(), 1)


class TestCHK(unittest.TestCase):
    def setUp(self):
        
    def test_chk_multipleA_1(self):
        self.assertEqual(checkout_solution.checkout("AAA"), 130)

    def test_chk_multipleA_2(self):
        self.assertEqual(checkout_solution.checkout("ABABA"), 130)

    def test_chk_multipleA_3(self):
        self.assertEqual(checkout_solution.checkout("ABBBBAA"), 130)

if __name__ == '__main__':
    unittest.main()
