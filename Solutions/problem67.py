# Project Euler Problem 67
# Created on: 2012-06-18
# Created by: William McDonald

def importTri():
    t = []
    f = open("problem67.txt")
    for line in f:
        t.append(map(int, line.split(" ")))
    return t

def getMax(lm, cur):
    l = len(cur) - 1
    maxL = [lm[0] + cur[0]]
    i = 1
    while True:
        if i == l:
            maxL.append(lm[i - 1] + cur[i])
            break
        maxL.append(max((lm[i - 1]), lm[i]) + cur[i])
        i += 1
    return maxL

def getAns():
    t = importTri()
    lmax = t[0]
    for i in range(1, len(t)):
        lmax = getMax(lmax, t[i])
    print(max(x for x in lmax))

getAns()
