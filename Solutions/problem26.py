# Project Euler Problem 26
# Created on: 2012-06-20
# Created by: William McDonald

def countRepeat(n):
    v = [0]*(10*n)
    div = 1
    while div < n: div *= 10
    count = 1
    while True:
        v[div - 1] = count
        div = (div - int(div/n)*n) * 10
        if div == 0: return 0
        if v[div - 1]: return (count - v[div-1])
        count += 1

def printAns():
    m = 0
    ans = 0
    for i in range(1, 1000):
        n = countRepeat(i)
        if n > m: m = n; ans = i
    print(ans)

printAns()
