import unittest

from solutions.CHK import checkout_solution

class TestCHK(unittest.TestCase):
    def test_removal_of_freebie(self):
        free = [(2, 'B', 1)]
        self.assertEquals(checkout_solution.remove_freebies_test("AAAAAEEBAAABB", 'E', free), "AAAAAEEBAAAB")

if __name__ == '__main__':
    unittest.main()
