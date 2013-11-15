from math import factorial

MIN_VAL = 1000000

FACTORIALS = [factorial(n) for n in xrange(0, 101)]
def choose(n, r):
    return FACTORIALS[n] / (FACTORIALS[r] * FACTORIALS[n - r])

def solve():
    numAns = 0
    minR = 10
    for n in xrange(23, 101):
        r = minR
        while choose(n, r) > MIN_VAL:
            r -= 1
        # We went one too far
        r += 1
        # Remember the minimum
        minR = min(r, minR)
        numAns += n - 2 * r + 1
    return numAns

print(solve())
