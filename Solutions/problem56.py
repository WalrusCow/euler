def sumDigits(n):
    ''' Sum the digits of n. '''
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def solve():
    m = 0
    for a in range(1, 100):
        for b in range(1, 100):
            m = max(m, sumDigits(a**b))
    return m

if __name__ == '__main__':
    print(solve())
