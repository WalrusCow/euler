# Project Euler Problem 13
# Created on: 2012-06-17
# Created by: William McDonald

def importNums():
    numFile = open("problem13.txt")
    numList = []
    for line in numFile:
        s = line
        lon = list(s)
        lon.pop()
        lon = map(int, lon)
        numList.append(lon)
    return numList

def longAddition(lst):
    ans = []
    last = 0
    while True:
        if lst[0] == []:
            break
        n = 0
        for i in lst:
            n += i.pop()
        n += last
        ans.append(n % 10)
        last = n / 10
    ans.append(last)
    return ans

nums = importNums()
ans = longAddition(nums)
print(ans)
