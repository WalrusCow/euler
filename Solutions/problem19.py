# Project Euler Problem 19
# Created on: 2012-06-18
# Created by: William McDonald

def getAns():
    d = 2
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = 0
    for y in range(1901, 2001):
        for m in range(12):
            if d == 0: s += 1
            d = (d + ms[m]) % 7
            if y % 4 == 0 and m == 1: d = (d + 1) % 7
    print(s)

getAns()