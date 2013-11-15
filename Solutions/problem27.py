# Project Euler Problem 27
# Created on: 2012-06-20
# Created by: William McDonald

# n^2 + a*n + b*n = prime for consecutive n start=0
# a must be odd, b must be prime

# Returns a list of all primes under n using a sieve technique
def primes(n):
    # True prime, False not
    primeSieve = [True] * (n / 2 - 1)
    primeList = [2]
    for i in range(3, n, 2):
        if primeSieve[(i - 3) / 2]:
            primeList.append(i)
            for j in range((i - 3) / 2 + i, len(primeSieve), i):
                primeSieve[j] = False
    return [primeList, primeSieve]

def numPrimes(f, ps):
    n = 0
    while True:
        a = f(n)
        if a < 0 or a % 2 == 0 or not ps[(a - 3) / 2]: break
        n += 1
    return n

def findAns():
    # max n, a, b
    max = [0, 0, 0]

    tmp = primes(100000)
    primeList, primeSieve = tmp[0], tmp[1]

    for b in primeList:
        if b > 999: break
        for a in range(999, -1000, -2):#(-(200 + b)/40) - 1, -2):#
            f = lambda x: x*x + x*a + b
            n = numPrimes(f, primeSieve)
            if n > max[0]: max = [n, a, b]
    print(max)
    return max[1]*max[2]

ans = findAns()
print(ans)
