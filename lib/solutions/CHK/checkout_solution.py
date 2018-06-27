import re

# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

# skus = unicode string
# normal = regular unit price
# product = character representing product
# special = a list of pairs (amount, special_offer) where amount is multiple and special offer
# @ return = the total price including any special offers
def get_totals(skus, product, normal, specials):
    p_count = skus.count(product)
    special_part = 0
    normal_part = 0
    if specials:
        for s in specials:
            if p_count > s[0]:
                num_this_special = (p_count/s[0])
                special_part = num_this_special * s[1]
                p_count -= (num_this_special * s[0])
            normal_part = (p_count % s[0]) * normal
    else:
        normal_part = p_count * normal

    total = special_part + normal_part
    return total

# noinspection PyUnusedLocal
# skus = unicode string
# @return = an Integer representing the total checkout value of the items
def checkout(skus):
    total = 0
    #invalid input = anything not ABCD
    if(re.match('^[ABCD]*$', skus)):
        total += get_totals(skus, 'A', 50, [(5, 200), (3,130)])
        total += get_totals(skus, 'B', 30, [(2, 45)])
        total += get_totals(skus, 'C', 20, [])
        total += get_totals(skus, 'D', 15, [])
    else:
        total = -1

    return total

