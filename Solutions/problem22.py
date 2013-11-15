# Project Euler Problem 22
# Created on: 2012-06-20
# Created by: William McDonald

from problem22names import *

def getAns():
    nameList.sort()
    zero = ord('A')
    total = 0
    for i in range(len(nameList)):
        s = 0
        for c in nameList[i]:
            s += (ord(c) - zero + 1)
        s *= (i + 1)
        total += s
    return total

ans = getAns()
print(ans)