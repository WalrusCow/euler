'''
euler.py
Random utilities written during euler questions.
'''

def permuteInts(L):
    ''' Permute a list of digits into integers. '''
    previous = set()
    def _permute(lst, acc):
        if not lst:
            yield acc
        for i, c in enumerate(lst):
            for perm in _permute(lst[:i] + lst[i+1:], acc*10 + c):
                if perm not in previous:
                    yield perm
                    previous.add(perm)
    return _permute(L, 0)

def digitize(n):
    ''' Return a list of the digits of an integer. '''
    l = []
    while(n):
        l.append(n % 10)
        n /= 10
    return l[::-1]

def undigitize(li):
    ''' Create a number from a list of digits. '''
    numDigits = len(li)
    return sum(d * 10**(numDigits - i - 1) for i, d in enumerate(li))

def slowPrimes(n):
    ''' Return: (primes, sieve) for primes under n
    The sieve has all numbers from 0 to n-1 in it
    '''
    # True prime, False not.
    primeSieve = [True] * n
    primeSieve[0] = False
    primeSieve[1] = False
    primeList = []
    for i in xrange(2, n):
        if primeSieve[i]:
            primeList.append(i)
            for j in xrange(2 * i, len(primeSieve), i):
                primeSieve[j] = False
    return primeList, primeSieve

def primes(n):
    ''' Return: (primes, sieve) for primes under n
    The sieve has no even numbers in it, and begins at 3
    '''
    # True prime, False not.
    primeSieve = [True] * (n / 2 - 1)
    primeList = [2]
    for i in xrange(3, n, 2):
        if primeSieve[(i - 3) / 2]:
            primeList.append(i)
            for j in xrange((i - 3) / 2 + i, len(primeSieve), i):
                primeSieve[j] = False
    return primeList, primeSieve

def rotate(n):
    ''' Rotate the number n.
    e.g. 123 -> 123, 231, 312
    This is a generator.
    '''
    digitList = digitize(n)
    for i in xrange(len(digitList)):
        yield undigitize(digitList[i:] + digitList[:i])
