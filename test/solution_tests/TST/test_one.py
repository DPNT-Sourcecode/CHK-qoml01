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
        self.assertEquals(checkout_solution.remove_freebies_test("EABCBDBE", 'E', free), "EACBDBE")

    def test_chk_free(self):
        self.assertEqual(checkout_solution.checkout("ABBBBAACCCEE"), 345)

    def test_chk_3A(self):
        newskus = "ABBBAACCCEE"
        self.assertEquals(checkout_solution.get_totals(newskus, 'A', 50, [(5, 200), (3,130)]), 130)

    # # 130 + 45 + 30 + 60 = 265

    def test_chk_3Bs(self):
        newskus = "ABBBAACCCEE"
        self.assertEquals(checkout_solution.get_totals(newskus, 'B', 30, [(2, 45)]), 75)

    def test_chk_8As(self):
        newskus = "AAAAAAAA"
        self.assertEquals(checkout_solution.get_totals(newskus, 'A', 50, [(5, 200), (3,130)]), 330)

    def test_chk_9As(self):
        newskus = "AAAAAAAAA"
        self.assertEquals(checkout_solution.get_totals(newskus, 'A', 50, [(5, 200), (3,130)]), 380)

    def test_removal_of_freebie(self):
        free = [(2, 'B', 1)]
        self.assertEquals(checkout_solution.remove_freebies_test("AAAAAEEBAAABB", 'E', free), "AAAAAEEAAABB")

    def test_check_mix_free(self):
        self.assertEquals(checkout_solution.checkout("AAAAAEEBAAABB"), 455)

    def test_remove_freebies(self):
        skus = "FFF"
        free = [(2, 'F', 1)]
        self.assertEquals(checkout_solution.remove_freebies_test(skus, 'F', free), "FF")

    def test_remove_freebies_none(self):
        skus = "EEFFA"
        free = [(2, 'F', 1)]
        self.assertEquals(checkout_solution.remove_freebies_test(skus, 'F', free), "EEFFA")

    def test_remove_freebies_multiple(self):
        skus = "FFFEEFFAFFF"
        free = [(2, 'F', 1)]
        self.assertEquals(checkout_solution.remove_freebies_test(skus, 'F', free), "FEEFFAFFF")

    def test_check_mix_free_bogof(self):
        self.assertEquals(checkout_solution.checkout("AAAAAEEBAAABBFFF"), 475)


if __name__ == '__main__':
    unittest.main()
