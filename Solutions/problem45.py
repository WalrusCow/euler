import math
def isPentagonal(k):
    n = (math.sqrt(24*k + 1) + 1) / 6
    return n.is_integer()

def hexagonal(n):
    return n*(2*n - 1)

def solve():
    n = 144
    while True:
        n += 1
        k = hexagonal(n)
        if isPentagonal(k):
            return n, k

print(solve())
