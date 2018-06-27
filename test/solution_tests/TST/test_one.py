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
        self.assertEqual(checkout_solution.checkout("ABBBBAACCC"), 280)

    def test_chk_multipleCD(self):
        self.assertEqual(checkout_solution.checkout("CDDD"), 65)

    def test_chk_lower(self):
        self.assertEqual(checkout_solution.checkout("BacdDDaa"), 225)

    def test_chk_empty_string(self):
        self.assertEqual(checkout_solution.checkout(""), 0)

    def test_chk_string_invalid_products(self):
        self.assertEqual(checkout_solution.checkout("EFG"), -1)

    def test_chk_lower(self):
        self.assertEqual(checkout_solution.checkout("bithika"), -1)

    def test_chk_mixed_lower_special(self):
        self.assertEqual(checkout_solution.checkout("BacdDDaa%-~+"), -1)

    def test_chk_5As(self):
        self.assertEqual(checkout_solution.checkout("AAAAA"), 200)

    def test_remove_p_from_list(self):
        self.assertEquals(checkout_solution.remove_product_from_list("ABCDEE", 'E'), "ABCDE")

    def test_remove_p_from_list(self):
        self.assertEquals(checkout_solution.remove_product_from_list("EABCDE", 'E'), "ABCDE")

    def test_remove_freebies(self):
        free = [(2, 'B', 1)]
        self.assertEquals(checkout_solution.remove_freebies("EABCBDBE", 'E', free), "EACBDBE")

if __name__ == '__main__':
    unittest.main()
