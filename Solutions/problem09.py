# Project Euler Problem 9
# Created on: 2012-06-14
# Created by: William McDonald

from functools import reduce
def fn():
    for j in range(500, 199, -1):
        k = 1000 - j
        for i in range(1, int(k / 2) + 1):
            if ((k - i) ** 2) + (i ** 2) == j ** 2:
                return[k - i, i, j]

prod = reduce(lambda x,y: x*y, fn(), 1)
print(prod)
