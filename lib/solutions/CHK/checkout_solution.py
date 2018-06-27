
def total_a(skus):




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

