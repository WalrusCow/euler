# Project Euler Problem 24
# Created on: 2012-06-20
# Created by: William McDonald

import math

def getAns(i):
    ans = 0
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in range(9, -1, -1):
        c = 0
        f = math.factorial(n)
        while i >= f:
            i -= f
            c += 1
        c = nums.pop(c)
        ans += c * 10 ** len(nums)
    return ans

print(getAns(999999))