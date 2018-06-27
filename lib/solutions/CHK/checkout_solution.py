

# noinspection PyUnusedLocal
# skus = unicode string
# @return = an Integer representing the total checkout value of the items
def checkout(skus):
    total = 0
    a_count = skus.toupper().count('A')
    special_a = (a_count/3) * 130
    
