# Project Euler Problem 3
# Created on: 2012-06-12
# Created by: William McDonald

def fact(a):
    x = []
    n = 3
    while a != 1:
        while a % n == 0:
            a /= n
            x.insert(0, n)
        n += 2
    return x

def moreFact(b):
    newFact=[]
    for n in b:
        x = fact(n)
        if x[0] != n:
            newFact.extend(x)
        else:
            newFact.append(n)
    return newFact

def findMaxPrime(a):
    x = fact(a)
    mx = moreFact(x)
    while x != mx:
        x = mx
        mx = moreFact(x)
    p = 0
    for n in x:
        p = n if n > p else p
    return p

number = 600851475143
maxPrime = findMaxPrime(number)

print(maxPrime)
