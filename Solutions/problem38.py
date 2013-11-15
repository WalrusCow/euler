from euler import digitize, undigitize

digitSet = set((1,2,3,4,5,6,7,8,9))

def multiples():
    ''' Find largest pandigital number formed as a concatenated product
    of an integer with (1, 2, ..., n) with n > 1
    '''
    maxProd = 918273645
    # Check up to 4 digit numbers
    for i in xrange(9111, 10000):
        prod = digitize(i)
        if prod[0] != 9:
            continue
        p = 2
        while(len(prod) < 9):
            prod += digitize(p * i)
            p += 1
        if isPandigital(prod):
            maxProd = max(undigitize(prod), maxProd)
    return maxProd

def isPandigital(lon):
    ''' Take in a list of numbers and determine if the list is pandigital. '''

    return len(lon) == 9 and set(lon) == digitSet

print(multiples())
