from fractions import Fraction

def numDigits(n):
    d = 0
    while n:
        d += 1
        n //= 10
    return d

def solve(maxDepth):
    ans = Fraction(1, 2)
    count = 0
    for _ in range(maxDepth):
        f = 1 + ans
        if numDigits(f.numerator) > numDigits(f.denominator):
            count += 1
        ans = Fraction(1, 2 + ans)
    return count

if __name__ == '__main__':
    print(solve(1001))
