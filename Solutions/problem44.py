import math
def pentagonal(n):
    ''' Compute the nth pentagonal number. '''
    return (n * (3*n - 1)) / 2

def isPentagonal(k):
    n = (math.sqrt(24*k + 1) + 1) / 6
    return int(n) if n.is_integer() else False

def solve():
    i = 1
    while True:
        i += 1
        for j in xrange(i, 0, -1):
            n = pentagonal(i)
            m = pentagonal(j)
            if isPentagonal(n+m) and isPentagonal(n-m):
                return (n, m, n-m)

print(solve())
