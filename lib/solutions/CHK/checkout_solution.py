
# skus = unicode string
# normal = regular unit price
# product = character representing product
# special = pair (amount, special_offer) where amount is multiple and special offer
# @ return = the total price including any special offers
def get_totals(skus, product, normal, special):
    p_count = skus.upper().count(product)
    if special:
        special_part = (p_count/special.first) * special.second
    normal_part = (p_count % special.first) * normal
    total = special_part + normal_part
    return total

# noinspection PyUnusedLocal
# skus = unicode string
# @return = an Integer representing the total checkout value of the items
def checkout(skus):
    total = 0
    total += get_totals(skus, 'A', 50, (3, 130))
    total += get_totals(skus, 'B', 30, (2, 45))
    total += get_totals(skus, 'C', 20, None)
    total += get_totals(skus, 'D', 15, None)
    return total

