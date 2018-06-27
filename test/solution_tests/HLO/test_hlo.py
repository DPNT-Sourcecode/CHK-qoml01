import unittest

from solutions.HLO_R2 import hello_solution


class TestHLO(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(hello_solution.compute(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
