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

# skus - the product list
# group_discount_products = the list of products belonging to this group discount, ordered by price high to low
# num = the number of products to remove
# @return the modified product list, with products removed according to the order given in the group
def remove_products_with_priority(skus, group_discount_products, num):
    new_skus = skus
    c = 0
    pos = 0
    for p in group_discount_products:
        print ('%r' % p )
        while(pos != -1 and c != num):
            pos = new_skus.find(p)
            if pos != -1:
                print('%r found at %d' % (p,pos))
                new_skus = new_skus.replace(p, '', 1)
                c += 1
                if c == num:
                    break
            else:
                pos = 0
                continue

    return new_skus


# skus = unicode string representing product list
# special_group = a list of tuples (group, multiple, offer) where:
#            group = list of products
#            multiple = how many of these products to get a special offer
#            offer = how much it costs
# @return a tuple of new product string with the special offer items removed, and a cost
def remove_special_group_test(skus, special_group):
    new_skus = skus

    p_count = 0
    for p in special_group[0]: # for each char in the group, count occurences
        p_count += skus.count(p)

    # now work out how many offers are scored
    # divide total count by special_group[1] (the multiple we're looking for)
    total = 0
    if p_count >= special_group[1]: # there's at least 1
        score = p_count / special_group[1]
        total = score * special_group[2] # num offers scored * price

    # now remove these items from the product list
    for n in range(p_count):
        new_skus = remove_products_with_priority(new_skus, special_group[0])
    print('returning %s' % new_skus)
    return (total, new_skus)




# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S ,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+

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
        ('K', 70, [(2, 150)], []),
        ('L', 90, [], []),
        ('M', 15, [], []),
        ('N', 40, [], [(3, 'M', 1)]),
        ('O', 10, [], []),
        ('P', 50, [(5,200)], []),
        ('Q', 30, [(3,80)], []),
        ('R', 50, [], [(3, 'Q', 1)]),
        ('S', 20, [], []),
        ('T', 20, [], []),
        ('U', 40, [], [(3, 'U', 1)]),
        ('V', 50, [(3, 130),(2, 90)], []),
        ('W', 20, [], []),
        ('X', 17, [], []),
        ('Y', 20, [], []),
        ('Z', 21, [], []),

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

