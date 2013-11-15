# Project Euler Problem 10
# Created on: 2012-06-14
# Created by: William McDonald

# Sum of all primes strictly smaller than n
def findSum(n):
    mark = ['0'] * ((n / 2) - 1)
    s = 2
    p = 3
    while p * p < n:
        if mark[(p / 2) - 1] == '0':
            v = (p / 2) - 1 + p
            s += p
            while v < len(mark):
                mark[v] = '1'
                v += p
        p += 2
    for i in range((p / 2) - 1, len(mark)):
        if mark[i] == '0':
            s += ((i + 1) * 2) + 1
    return s

ans = findSum(2000000)
print(ans)