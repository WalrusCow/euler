# Lowest sum of a set of 5 primes where any two concatenate to produce a prime

from collections import defaultdict

from euler import PrimeSieve

def _num_digits(n):
    ''' Number of digits in a positive number < 10 billion.'''
    for x in range(6, 0, -1):
        if n > 10 ** x:
            return x + 1
    return 1


def _concat_nums(p1, p2):
    return p1 * (10 ** _num_digits(p2)) + p2


def solve_p60():
    sieve = PrimeSieve(10**4)

    concat_pairs = defaultdict(set)
    for (idx, p) in enumerate(sieve.primes):
        concat_pairs[p].add(p)
        for p2 in sieve.primes[idx+1:]:
            if (
                sieve.is_prime(_concat_nums(p, p2)) and
                sieve.is_prime(_concat_nums(p2, p))
            ):
                concat_pairs[p].add(p2)
                concat_pairs[p2].add(p)

    candidate_sets = []
    concat_pairs = sorted(pair for pair in concat_pairs.items())
    for i1, (p1, s1) in enumerate(concat_pairs):
        cs1 = s1
        for i2 in range(i1 + 1, len(concat_pairs)):
            p2, s2 = concat_pairs[i2]
            cs2 = cs1 & s2
            if len(cs2) < 5: continue
            for i3 in range(i2 + 1, len(concat_pairs)):
                p3, s3 = concat_pairs[i3]
                cs3 = cs2 & s3
                if len(cs3) < 5: continue
                for i4 in range(i3 + 1, len(concat_pairs)):
                    p4, s4 = concat_pairs[i4]
                    cs4 = cs3 & s4
                    if len(cs4) < 5: continue
                    for i5 in range(i4 + 1, len(concat_pairs)):
                        p5, s5 = concat_pairs[i5]
                        cs5 = cs4 & s5
                        if len(cs5) < 5: continue
                        primes = (p1, p2, p3, p4, p5)
                        candidate_sets.append((sum(primes), primes))
    if not candidate_sets:
        return None
    candidate_sets.sort()
    prime_sum, primes = candidate_sets[0]
    print('Lowest primes: {}'.format(', '.join(map(str, primes))))
    return prime_sum


if __name__ == '__main__':
    ans = solve_p60()
    if ans is not None:
        print('The answer is {}'.format(ans))
