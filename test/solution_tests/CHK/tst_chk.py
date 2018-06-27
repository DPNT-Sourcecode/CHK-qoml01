import unittest

from solutions.CHK import chk_solution


class TestCHK(unittest.TestCase):
    def test_chk(self):
        self.assertEqual(chk_solution.checkout(fn), "Hello, Mr. X!")

if __name__ == '__main__':
    unittest.main()
