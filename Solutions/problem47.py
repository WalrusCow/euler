from euler import primes, slowPrimes
MAGIC = 4

# Compute primes below 100000
primeList, primeSieve = slowPrimes(1000000)

# Returns a list of prime factors of n
def primeD(n):
    plst = []
    if primeSieve[n]: return []
    for p in primeList:
        if not (n % p):
            plst.append(p)
        while n % p == 0:
            n /= p
        if n == 1:
            return plst
        if len(plst) > MAGIC:
            return []

def solve():
    ''' Solve problem 47.
    We will just check all numbers to see which ones have 4 distinct prime
    factors.
    '''

    n = 2*3*5*7
    run = 0
    while True:
        n += 1
        divList = primeD(n)
        if len(divList) == MAGIC:
            run += 1
        else:
            run = 0
        if run == MAGIC:
            return n - run + 1

print(solve())
