import math
from euler import PrimeSieve


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
