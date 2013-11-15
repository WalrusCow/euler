# Project Euler Problem 12
# Created on: 2012-06-15
# Created by: William McDonald

import math

# Short list of prime numbers under 20
primeList = [2, 3, 5, 7, 9, 11, 13, 17, 19]
last = 21

# Returns True if n is prime, otherwise False
def isPrime(n):
    prime = True
    for i in primeList:
        if n % i == 0:
            prime = False
            break
        if i > math.floor(math.sqrt(n)):
            break
    return prime

# Return the powers of the divisors of n in a list
def divisors(n):
    global last
    while last <= n:
        if isPrime(last):
            primeList.append(last)
        last += 2
    lst = []
    for i in primeList:
        c = 0
        while n % i == 0:
            n /= i
            c += 1
        lst.append(c)
    return lst

# Returns the number of divisors of two numbers
# represented by lists of the exponents of their
# prime factorization
def numDivisors(l1, l2):
    lst = []
    while len(l1) < len(l2):
        l1.append(0)
    while len(l2) < len(l1):
        l2.append(0)
    for i in range(len(l1)):
        lst.append(l1[i] + l2[i] + 1)
    lst[0] -= 1
    return reduce(lambda x, y: x * y, lst, 1)

def findAns():
    n = 1
    m = n + 1
    d = 0
    dn = divisors(n)
    while d <= 500:
        dm = divisors(m)
        d = numDivisors(dn, dm)
        if d > 500:
            return (n * m) / 2
        n, m = m, m + 1
        dn = dm

ans = findAns()
print(ans)
