import math
from euler import primes

MAX_NUM = 7654321
PRIME_LIST = primes(int(math.sqrt(MAX_NUM)) + 1)[0]
DIGITS = set(xrange(1,8))

def isPrime(i):
    return not any(i % p == 0 for p in PRIME_LIST)

def permuteInts(s):
    def _permute(aSet, acc):
        if not aSet:
            yield acc
        for c in aSet:
            for perm in _permute(aSet.difference(set((c,))), acc*10 + c):
                yield perm
    return _permute(set(s), 0)

print(max(p for p in permuteInts(DIGITS) if isPrime(p)))
