# Project Euler Problem 7
# Created on: 2012-06-13
# Created by: William McDonald

import math
import time

# Short list of prime numbers under 20
primeList = [2, 3, 5, 7, 9, 11, 13, 17, 19]

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

# Returns the nth prime number
def getPrime(n):
    if n < len(primeList):
        return primeList[n - 1]
    else:
        p = primeList[len(primeList) - 1] + 2
        while len(primeList) <= n:
            if isPrime(p):
                primeList.append(p)
            p += 2
        return primeList[len(primeList) - 1]

start = time.time()
ans = getPrime(10001)
cost = time.time() - start
print(ans)
print("Time: {}".format(cost))