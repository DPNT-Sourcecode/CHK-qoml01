import unittest

from solutions.CHK import checkout_solution

class TestCHK(unittest.TestCase):
    def test_removal_of_freebie(self):
        free = [(2, 'B', 1)]
        self.assertEquals(checkout_solution.remove_freebies_test("AAAAAEEBAAABB", 'E', free), "AAAAAEEAAABB")

    def test_check_mix_free(self):
        self.assertEquals(checkout_solution.checkout("AAAAAEEBAAABB"), 455)

    def test_check_product_list(self):
        self.assertEquals(checkout_solution.checkout("HHHHHHHHHHHH"), 100)

    def test_check_product_list(self):
        self.assertEquals(checkout_solution.checkout("HHHHHHHHHHHH"), 100)

if __name__ == '__main__':
    unittest.main()
