import unittest

from solutions.TST import one
from solutions.CHK import checkout_solution

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(one.get(), 1)


class TestCHK(unittest.TestCase):
    def test_chk_multipleA(self):
        self.assertEqual(checkout_solution.checkout("AAA"), 130)

if __name__ == '__main__':
    unittest.main()
