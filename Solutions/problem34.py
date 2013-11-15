from math import factorial
# consider up to 7 digit numbers

def digitize(n):
    l = []
    while(n):
        l.append(n % 10)
        n /= 10
    return l[::-1]

def countFacts():
    nineFacts = [factorial(9) * i for i in xrange(1, 7)]
    theFacts = [factorial(i) for i in xrange(10)]
    endSum = 0
    for x in xrange(10, 45000):
        s = 0 # fact sum
        digits = digitize(x)
        numD = len(digits)
        for i, d in enumerate(digits):
            s += theFacts[d]
            if nineFacts[numD - i - 1] < (x - s):
                break
        if s == x:
            endSum += s
    return endSum

print(countFacts())
