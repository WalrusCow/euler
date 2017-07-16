# Lowest sum of a set of 5 primes where any two concatenate to produce a prime

from euler import PrimeSieve

def _num_digits(n):
    ''' Number of digits in a positive number < 10 billion.'''
    for x in range(10, 0, -1):
        if n > 10 ** x:
            return x + 1
    return 1


def _concat_nums(p1, p2):
    return p1 * (10 ** _num_digits(p2)) + p2


class ConcatPrimeSet():
    def __init__(self, sieve):
        self.primes = set()
        self._impossible_pairs = set()
        self._sieve = sieve


    def reset_primes(self):
        self.primes = set()


    def try_add_prime(self, p):
        for set_mem in self.primes:
            if (set_mem, p) in self._impossible_pairs:
                return False
        for set_mem in self.primes:
            p1_to_test = _concat_nums(set_mem, p)
            p2_to_test = _concat_nums(p, set_mem)
            for x in (p1_to_test, p2_to_test):
                if not self._sieve.is_prime(x):
                    self._impossible_pairs.add((set_mem, p))
                    return False
        self.primes.add(p)
        return True


def solve_p60():
    sieve = PrimeSieve(10 ** 6)
    prime_set = ConcatPrimeSet(sieve)
    for (idx, p) in enumerate(sieve.primes):
        print('Got to size {} - now trying {}'.format(len(prime_set.primes), p))
        prime_set.reset_primes()
        prime_set.try_add_prime(p)
        for p2 in sieve.primes[idx:]:
            prime_set.try_add_prime(p2)
            if len(prime_set.primes) >= 5:
                print('Size is {}'.format(len(prime_set.primes)))
                print('Primes are {}'.format(', '.join(
                    map(str, prime_set.primes))
                ))
                print('Sum is {}'.format(sum(prime_set.primes)))
                return


if __name__ == '__main__':
    solve_p60()
