import unittest

from solutions.CHK import checkout_solution


class TestCHK(unittest.TestCase):
    def test_chk_multipleA(self):
        self.assertEqual(chk_solution.checkout("AAA"), 130)

if __name__ == '__main__':
    unittest.main()
