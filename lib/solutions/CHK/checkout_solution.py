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
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+

#ABBBAACCCEE

# 130 + 45 + 30 + 60 = 265

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

# skus = unicode string representing product list
# product = the product to look for
# freebies = a list of tuples (amount, free_product, free_amount) where amount is multiple of cur product being checked,
#            free_product = product to get for free, free_amount how many you get
# if free_product == product, then removal occurs only if amount+free_amount products are in skus
# @return a new product string with the free items removed
def remove_freebies_test(skus, product, freebies):
    new_skus = skus
    p_count = skus.count(product)
    if freebies:
        for f in freebies:
            if product==f[1]: # if this is bogof, then check we have minimum
               min = f[0]+f[2]
            else:
               min = f[0]

            # count multiples of product, and remove free products from original string
            if p_count >= min: # then we have at least 1 freebie
                num_this_freebie = (p_count/min) # this many freebies
                free_amount = num_this_freebie*f[2] # remove this many freebies from list
                print('remove this many %d' % free_amount)
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
                special_part += num_this_special * s[1]
                p_count -= (num_this_special * s[0])
        if p_count:
            normal_part = (p_count % s[0]) * normal
    else:
        normal_part = p_count * normal

    total = special_part + normal_part
    return total




# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

# noinspection PyUnusedLocal
# skus = unicode string
# @return = an Integer representing the total checkout value of the items
def checkout(skus):

    # items will be a list of tuples: product name, regular price, offers, freebies
    items = [
        ('A', 50, [(5, 200), (3,130)], []),
        ('B', 30, [(2, 45)], []),
        ('C', 20, [], []),
        ('D', 15, [], []),
        ('E', 40, [], [(2, 'B', 1)]),
        ('F', 10, [], [(2, 'F', 1)]),
        ('G', 20, [], []),
        ('H', 10, [(10, 80),(5, 45)], []),
        ('I', 35, [], []),
        ('J', 60, [], []),
        ('K', 80, [(2, 150)], []),
        ('L', 90, [], []),
        ('M', 15, [], []),
        ('N', 40, [], [(3, 'M', 1)]),
        ('O', 10, [], []),
        ('P', 50, [(5,200)], []),
        ('Q', 30, [(3,80)], []),
        ('R', 50, [], [(3, 'Q', 1)]),
        ('S', 30, [], []),
        ('T', 20, [], []),
        ('U', 40, [], [(3, 'U', 1)]),
        ('V', 50, [(3, 130),(2, 90)], []),
        ('W', 20, [], []),
        ('X', 90, [], []),
        ('Y', 10, [], []),
        ('Z', 50, [], []),

    ]

    #invalid input = anything not in alphabet
    all_products = [x[0] for x in items]

    if(re.match('^[ABCDEFGHIJKLMNOPQRSTUVWXYZ]*$', skus)):

        # first, remove the freebies
        # for each item:
        #    if it has a freebie list
        #    remove them from the lst
        #
        # then, proess the totals, and offers
        # for each item:
        #    add the total via get_totals
        newskus = skus
        for p in items:
            if p[3]: # there is a freebies list
                newskus = remove_freebies_test(newskus, p[0], p[3])
        total = 0
        for p in items:
            total += get_totals(newskus, p[0], p[1], p[2])

        # free = [(2, 'B', 1)]
        # newskus = remove_freebies_test(skus, 'E', free)
        # free = [(2, 'F', 1)]
        # newskus = remove_freebies_test(newskus, 'F', free)
        # print('after removing freebies %s' % newskus)
        # total += get_totals(newskus, 'A', 50, [(5, 200), (3,130)])
        # total += get_totals(newskus, 'B', 30, [(2, 45)])
        # total += get_totals(newskus, 'C', 20, [])
        # total += get_totals(newskus, 'D', 15, [])
        # total += get_totals(newskus, 'E', 40, [])
        # total += get_totals(newskus, 'F', 10, [])
    else:
        total = -1

    return total

