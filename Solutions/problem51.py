'''
Must have the number of digits replaced being a multiple
of 3.  Since the sum of the digits must be not congruent to
0 mod 3, so if we consider the sum of the other digits being
k = a mod 3 then we have k + nd = a + nd mod 3 for at least
8 possible d's.  But then we cannot have 3 d's that result
in 0 mod 3, which would happen for any n coprime with 3.
'''

from collections import Counter
from euler import slowPrimes, digitize, undigitize

FAMILY_SIZE = 8

# Precompute all primes up to one million
primeList, primeSieve = slowPrimes(1000000)

def possible(p):
    # We know this lower bound from the question statement
    if p < 56000: return False
    digits = digitize(p)
    digitCount = Counter(digits)
    # Possible digits are ones that are repeated a multiple of 3 times
    possibleDigits = {d for d, c in digitCount.items() if c % 3 == 0}
    return possibleDigits

def listReplace(li, rep, new):
    # Replace rep in li with new
    return [new if x == rep else x for x in li]

def solve():
    potentialPrimes = []
    # Compute potential candidates (could be sped up by removing this)
    for p in primeList:
        possibleDigits = possible(p)
        if possibleDigits:
            potentialPrimes.append((p, possibleDigits))

    # Loop through potential primes
    for p, digitList in potentialPrimes:
        digits = digitize(p)
        for d in digitList:
            # Count the size of the family
            familySize = 0
            for i in xrange(10):
                # Replace the desired digits
                newDigits = listReplace(digits, d, i)
                newNum = undigitize(newDigits)
                # Make sure that we are not replacing the leading
                # number with a 0
                if len(digitize(newNum)) < len(digits):
                    continue
                if primeSieve[newNum]:
                    familySize += 1
            if familySize >= FAMILY_SIZE:
                return p

    # No answer found...
    return None

print(solve())
