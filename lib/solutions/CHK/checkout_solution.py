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


# skus = unicode string representing product list
# prod = the product to remove
# num = the number to remove
# @return the new product string after removal
def remove_product_from_list(skus, prod):
    print ('%r, %r' % (skus, prod))
    final = skus
    p = final.find(prod)
    if p != -1:
        print ('at pos %d' % p)
        new_skus_top = skus[:p]
        new_skus_btm = skus[p+1:]
        final = new_skus_top + new_skus_btm
    else:
        print ('at pos %d' % p)
    return final

# skus = unicode string representing product list
# product = the product to look for
# freebies = a list of tuples (amount, free_product, free_amount) where amount is multiple of cur product being checked,
#            free_product = product to get for free, free_amount how many you get
# @return a new product string with the free items removed
def remove_freebies(skus, product, freebies):
    new_skus = skus
    p_count = skus.count(product)
    if freebies:
        for f in freebies:
            # count multiples of product, and remove free products from original string
            if p_count >= f[0]: # then we have at least 1 freebie
                num_this_freebie = (p_count/f[0]) # this many freebies
                free_amount = num_this_freebie*f[2] # remove this many freebies from list
                free_product = f[1]
                for n in range(free_amount):
                    new_skus = remove_product_from_list(new_skus, free_product)
    print('returning %s' % new_skus)
    return new_skus

# skus = unicode string
# normal = regular unit price
# product = character representing product
# specials = a list of pairs (amount, special_offer) where amount is multiple and special offer
# @ return = the total price including any special offers
def get_totals(skus, product, normal, specials):
    p_count = skus.count(product)
    special_part = 0
    normal_part = 0
    if specials:
        for s in specials:
            if p_count >= s[0]:
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
    if(re.match('^[ABCDE]*$', skus)):
        free = [(2, 'B', 1)]
        newskus = remove_freebies(skus, 'E', free)
        total += get_totals(newskus, 'A', 50, [(5, 200), (3,130)])
        total += get_totals(newskus, 'B', 30, [(2, 45)])
        total += get_totals(newskus, 'C', 20, [])
        total += get_totals(newskus, 'D', 15, [])
    else:
        total = -1

    return total

