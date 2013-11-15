# Project Euler Problem 11
# Created on: 2012-06-14
# Created by: William McDonald

# Return the minimum number that can be present in
# a solution set of four numbers
def getMin(cap, min):
    k = 99 * 99 * 99
    for i in range(min, 99):
        if i * k > cap:
            return i

def importGrid():
    f = open("problem11.txt")
    grid = []
    for line in f:
        str = line
        lon = str.split(" ")
        i = 0
        for n in lon:
            lon[i] = int(n)
            i += 1
        grid.append(lon)
    f.close()
    return grid

def transpose(g):
    return map(list, zip(*g))

def makeDiagGrid(g):
    n = []
    for i in range(3, len(g)):
        temp = []
        for j in range(i, -1, -1):
            temp.append(g[j][i - j])
        n.append(temp)
    for i in range(1, len(g) - 3):
        temp = []
        for j in range(0, len(g) - i):
            temp.append(g[i + j][len(g) - 1 - j])
        n.append(temp)

    return n

def getAns():
    # Cursory examination: 94 * 99 * 71 * 61
    max = 94 * 99 * 71 * 61
    min = getMin(max, 0)

    udg = importGrid()
    lrg = transpose(udg)
    dg1 = makeDiagGrid(lrg)
    lrg.reverse()
    dg2 = makeDiagGrid(lrg)
    grids = [udg, lrg, dg1, dg2]
    for g in grids:
        prod = 1
        i = 0
        while i < len(g):
            j = 0
            lst = g[i]
            while j < (len(lst) - 3):
                for k in range(4):
                    if lst[j + k] < min:
                        j += k
                        break
                    else:
                        prod *= lst[j + k]
                else:
                    if prod > max:
                        max = prod
                        min = getMin(max, min)
                j += 1
                prod = 1
            i += 1
    return max

ans = getAns()
print(ans)
