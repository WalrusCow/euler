# Project Euler Problem 15
# Created on: 2012-06-17
# Created by: William McDonald

from math import factorial

# Paths through an nxn grid
def paths(n):
    a = factorial(n)
    a *= a
    b = factorial(2 * n)
    return int(b / a)

ans = paths(20)
print(ans)
