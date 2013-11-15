# Project Euler Problem 23
# Created on: 2012-06-20
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
def sumD(n):
    lop = primeD(n)
    sum = 1
    for i in range(len(lop)):
        sum *= (lop[i][0] ** (lop[i][1] + 1)) - 1
        sum /= (lop[i][0] - 1)
    return (sum - n)

# Returns a sieve and list of all abundant numbers under n
def listAbundant(n):
    sieve = [False] * n
    lst = []

    for i in range(1, n):
        if sumD(i) > i:
            sieve[i - 1] = True
            lst.append(i)

    return [sieve, lst]

# Returns sum of all numbers below n that cannot be written
# as the sum of two abundant numbers
def getSum(n, sieve, lst):
    total = 0
    for i in range(1, n):
        for a in lst:
            if i - a < 12:
                total += i
                break
            if sieve[(i - a) - 1]:
                break
    return total

def printAns(n):
    tmp = listAbundant(n)
    lst = tmp.pop()
    sieve = tmp.pop()
    ans = getSum(n, sieve, lst)
    print(ans)

primeList = primes(20162)
printAns(20162)
