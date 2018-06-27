import unittest

from solutions.HLO import hello_solution


class TestHLO(unittest.TestCase):
    def test_hlo(self):
        fn = '"Mr. X"'
        self.assertEqual(hello_solution.hello(fn), "Hello, Mr. X!")

if __name__ == '__main__':
    unittest.main()
