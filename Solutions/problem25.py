# Project Euler Problem 25
# Created on: 2012-06-20
# Created by: William McDonald

def getAns():
    fib1 = 1
    fib2 = 1
    t = 2
    while fib2 < (10 ** 999):
        fib1, fib2 = fib2, fib1 + fib2;
        t += 1
    print(t)

getAns()