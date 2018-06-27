import re

# skus = unicode string
# normal = regular unit price
# product = character representing product
# special = pair (amount, special_offer) where amount is multiple and special offer
# @ return = the total price including any special offers
def get_totals(skus, product, normal, special):
    p_count = skus.count(product)
    special_part = 0
    normal_part = 0
    if special:
        special_part = (p_count/special[0]) * special[1]
        normal_part = (p_count % special[0]) * normal
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
        total += get_totals(skus, 'A', 50, (3, 130))
        total += get_totals(skus, 'B', 30, (2, 45))
        total += get_totals(skus, 'C', 20, None)
        total += get_totals(skus, 'D', 15, None)
    else:
        total = -1

    return total

