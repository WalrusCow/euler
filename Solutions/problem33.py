from fractions import Fraction
from functools import reduce

def findCancelling():
    # Need num/denom with at least one digit in common
    # but not the same or multiple of 10
    # i.e. no 0's

    fracList = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j: continue
            num = i * 10 + j
            for k in range(1, 10):
                denom = i * 10 + k
                if checkFraction(num, denom, i):
                    fracList.append(Fraction(num, denom))
                denom = k * 10 + i
                if checkFraction(num, denom, i):
                    fracList.append(Fraction(num, denom))
                denom = k * 10 + j
                if checkFraction(num, denom, j):
                    fracList.append(Fraction(num, denom))
                denom = j * 10 + k
                if checkFraction(num, denom, j):
                    fracList.append(Fraction(num, denom))
    return fracList

def checkFraction(num, denom, digit):
    original = Fraction(num, denom)
    if original >= 1: return False

    dig = str(digit)
    n1 = str(num).replace(dig, '')
    n2 = str(denom).replace(dig, '')
    if not (n1 and n2):
        return False
    if Fraction(int(n1), int(n2)) == original:
        return True

fracList = findCancelling()
print(fracList)
print(reduce(lambda x, y: x*y, fracList, 1))

