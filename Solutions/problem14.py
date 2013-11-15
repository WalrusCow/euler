# Project Euler Problem 14
# Created on: 2012-06-17
# Created by: William McDonald

import time

def countCollatz(n):
    c = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        c += 1
    return c

mx = 0
r = 0
a=time.time()
for i in range(999999, 500000, -2):
    c = countCollatz(i)
    if c > mx:
        mx = c
        r = i
print(r)
print("Time: {}".format(time.time()-a))
