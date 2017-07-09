import math

# We want to find the first side length of the square where the diagonal numbers
# both have less than 10% primes

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


def is_prime(n, primes):
    ''' Check if n is prime using a sorted list of primes. '''
    largest_to_check = math.ceil(math.sqrt(n))
    for p in primes:
        if p > largest_to_check:
            return True
        if n % p == 0:
            return False
    return False


class NumberSpiral():
    ''' Represents the diagonals of a number spiral, which goes clockwise
    starting from the bottom. '''
    def __init__(self):
        self.side_length = 3
        self._tr = 7
        self._tr_length = 2

        self._bl = 3
        self._bl_length = 1

        self._tl = 5
        self._tl_length = 1

        self._br = 9
        self._br_length = 2

        self._sieve = PrimeSieve(100000)

        self._tl_prime_count = 1
        self._br_prime_count = 0
        self._tr_prime_count = 1
        self._bl_prime_count = 1


    # Amount to increment to get the next number in each diagonal is:
    # Top Left: 8n + 4
    # Bottom Left: 8n + 2
    # Top Right: 8n - 2
    # Bottom Right: 8n
    # (Where n is the length of each diagonal so far)
    def _br_inc(self):
        inc = 8 * self._br_length
        self._br += inc
        self._br_length += 1
        if self._sieve.is_prime(self._br):
            self._br_prime_count += 1


    def _bl_inc(self):
        inc = 8 * self._bl_length + 2
        self._bl += inc
        self._bl_length += 1
        if self._sieve.is_prime(self._bl):
            self._bl_prime_count += 1


    def _tr_inc(self):
        inc = 8 * self._tr_length - 2
        self._tr += inc
        self._tr_length += 1
        if self._sieve.is_prime(self._tr):
            self._tr_prime_count += 1


    def _tl_inc(self):
        inc = 8 * self._tl_length + 4
        self._tl += inc
        self._tl_length += 1
        if self._sieve.is_prime(self._tl):
            self._tl_prime_count += 1


    def increment(self):
        self.side_length += 2
        if self.side_length > len(self._sieve):
            print(
                'Side length {} is too big for sieve.'
                ' Doubling sieve size to {}'.format(
                    self.side_length,
                    len(self._sieve) * 2
                )
            )
            print('Ratio: {}'.format(self.prime_ratio()))
            print('Prime counts: {} {} {} {}'.format(
                self._tr_prime_count,
                self._tl_prime_count,
                self._br_prime_count,
                self._bl_prime_count
            ))
            self._sieve = PrimeSieve(len(self._sieve) * 2)

        self._tl_inc()
        self._br_inc()
        self._bl_inc()
        self._tr_inc()


    def prime_ratio(self):
        unique_nums = self.side_length * 2
        if self.side_length % 2 == 1:
            unique_nums -= 1

        return (
            self._tr_prime_count + self._bl_prime_count
            + self._tl_prime_count + self._br_prime_count
        ) / unique_nums


def solve_p58():
    spiral = NumberSpiral()
    while spiral.prime_ratio() >= 0.1:
        spiral.increment()

    print('Side length: {}. Ratio: {}'.format(
        spiral.side_length,
        spiral.prime_ratio()
    ))


if __name__ == '__main__':
    solve_p58()
