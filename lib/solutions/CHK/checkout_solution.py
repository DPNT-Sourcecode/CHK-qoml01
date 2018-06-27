
# skus = unicode string
# normal = regular unit price
# product = character representing product
# special = pair (amount, special_offer) where amount is multiple and special offer
def totals(skus, product, normal, special):
    p_count = skus.upper().count(product)
    specials = (p_count/special.first) * special.second
    normal_a = (p_count % special.first) * normal
    total = special_a + normal_a



# noinspection PyUnusedLocal
# skus = unicode string
# @return = an Integer representing the total checkout value of the items
def checkout(skus):
    total = 0
    a_count = skus.upper().count('A')
    special_a = (a_count/3) * 130
    normal_a = (a_count % 3) * 50
    total = special_a + normal_a



    return total

