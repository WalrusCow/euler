# Project Euler Problem 21
# Created on: 2012-06-18
# Created by: William McDonald

# Returns a list of all primes under n using a sieve technique
def primes(n):
    # 0 prime, 1 not.
    primeSieve = ['0'] * (n / 2 - 1)
    primeList = [2]
    for i in range(3, n, 2):
        if primeSieve[(i - 3) / 2] == '0':
            primeList.append(i)
            for j in range((i - 3) / 2 + i, len(primeSieve), i):
                primeSieve[j] = '1'
    return primeList

# Returns a list of prime factors of n and their multiplicities
def primeD(n):
    plst = []
    for p in primeList:
        count = 0
        while n % p == 0:
            count += 1
            n /= p
        if count != 0:
            plst.append([p, count])
        if n == 1:
            return plst

# Returns the sum of all proper divisors of n
def sumD(n, primeList):
    lop = primeD(n, primeList)
    sum = 1
    for i in range(len(lop)):
        sum *= (lop[i][0] ** (lop[i][1] + 1)) - 1
        sum /= (lop[i][0] - 1)
    return (sum - n)

def getAns():
    primeList = primes(10000)
    total = 0
    for i in range(2, 10001):
        s1 = sumD(i, primeList)
        if s1 > i and s1 <= 10000:
            s2 = sumD(s1, primeList)
            if s2 == i: total += (s2 + s1)
    print(total)

getAns()