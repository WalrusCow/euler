# Project Euler Problem 4
# Created on: 2012-06-12
# created by: William McDonald

def numList(n):
    lst = []
    while n != 0:
        lst.append(n % 10)
        n /= 10
    return lst

def isPal(n):
    digits = 0
    for i in range(10):
        if 10 ** i > n:
            digits = i
            break

    if digits == 1:
        return True

    split = digits / 2

    front = n / (10 ** split) # left digits
    back = n % (10 ** split) # right digits

    front = numList(front)
    back = numList(back)
    back.reverse()

    if front == back:
        return True
    else:
        return False

cap = 999
for i in range(0, 200):
    result = False
    for j in range(0, 200):
        p = (cap - i) * (cap - j)
        result = isPal(p)
        if result:
            print(p)
            break
    if result:
        break

print("Done.")
