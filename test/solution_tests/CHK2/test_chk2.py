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

    def test_check_product_list_freebies(self):
        # 3 N's get you a free M
        self.assertEquals(checkout_solution.checkout("NNNM"), 120)

    def test_check_product_list_freebies_and_offers(self):
        # 3 N's get you a free M
        # P worth 50, and 5 for 200 (so 6 = 250)
        self.assertEquals(checkout_solution.checkout("NNNMPPPPPP"), 370)

    def test_check_product_list_no_offers_no_freebies(self):
        # a J is worth 60
        self.assertEquals(checkout_solution.checkout("J"), 60)

    def test_remove_group_discount_priority(self):
        self.assertEquals(checkout_solution.remove_products_with_priority("STXYZ", "ZYTSX", 1), "STXY")

    def test_remove_group_discount_priority_multiple(self):
        self.assertEquals(checkout_solution.remove_products_with_priority("ZSTXYZ", "ZYTSX", 2), "STXY")

    def test_remove_group_discount_priority_limit(self):
        self.assertEquals(checkout_solution.remove_products_with_priority("ZSTXYZABC", "ZYTSX", 8), "ABC")

    # def test_check_special_group_offers(self):
    #     sgo = ("STXYZ", 3, 45)
    #     self.assertEquals(checkout_solution.remove_special_group_test("STXYZ", sgo), (45, "YZ"))

if __name__ == '__main__':
    unittest.main()
