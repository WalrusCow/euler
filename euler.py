'''
euler.py
Random utilities written during euler questions.
'''

import math

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
    '''
    Return a list of the digits of an integer.
    The first item is the 1's column.
    '''
    l = []
    while(n):
        l.append(n % 10)
        n //= 10
    return l


def undigitize(li):
    '''
    Create a number from a list of digits.
    The first item should be the 1's column
    '''
    ans = 0
    m = 1
    for d in li:
        ans += d * m
        m *= 10
    return ans


def slowPrimes(n):
    ''' Return: (primes, sieve) for primes under n
    The sieve has all numbers from 0 to n-1 in it
    '''
    # True prime, False not.
    primeSieve = [True] * n
    primeSieve[0] = False
    primeSieve[1] = False
    primeList = []
    for i in range(2, n):
        if primeSieve[i]:
            primeList.append(i)
            for j in range(2 * i, len(primeSieve), i):
                primeSieve[j] = False
    return primeList, primeSieve


def primes(n):
    ''' Return: (primes, sieve) for primes under n
    The sieve has no even numbers in it, and begins at 3
    '''
    # True prime, False not.
    primeSieve = [True] * (n // 2 - 1)
    primeList = [2]
    for i in range(3, n, 2):
        if primeSieve[(i - 3) // 2]:
            primeList.append(i)
            for j in range((i - 3) // 2 + i, len(primeSieve), i):
                primeSieve[j] = False
    return primeList, primeSieve


def rotate(n):
    ''' Rotate the number n.
    e.g. 123 -> 123, 231, 312
    This is a generator.
    '''
    digitList = digitize(n)
    for i in range(len(digitList)):
        yield undigitize(digitList[i:] + digitList[:i])


def isPalindrome(li):
    ''' Determine if a list is a palindrome. '''

    # We don't need to check the middle elem
    l = len(li)
    for i in range(l // 2):
        if li[i] != li[l - 1 - i]:
            return False
    return True


class PrimeSieve():
    def __init__(self, sieve_size):
        self._sieve = [True] * (sieve_size // 2)
        self._sieve[0] = False
        self.primes = [2]
        for idx in range(len(self._sieve)):
            if not self._sieve[idx]:
                continue
            n = idx * 2 + 1
            self.primes.append(n)
            not_prime = n + n + n
            while not_prime < sieve_size:
                self._sieve[not_prime // 2] = False
                not_prime += n + n
        print('Constructed sieve size {}'.format(sieve_size))


    def is_prime(self, n):
        if n % 2 == 0:
            return n == 2
        if n <= 1:
            return False
        if n < len(self):
            return self._sieve[n // 2]
        largest_prime_to_check = math.ceil(math.sqrt(n))
        if largest_prime_to_check > len(self):
            raise ValueError(
                'Sieve length {} too small to check primality of {}'.format(
                    len(self),
                    n,
                )
            )
        for p in self.primes:
            if p > largest_prime_to_check:
                return True
            if n % p == 0:
                return False
        return False



    def __len__(self):
        return len(self._sieve) * 2
