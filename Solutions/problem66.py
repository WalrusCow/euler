import itertools
import math

from fractions import Fraction

def _find_fraction_period_helper(n, nume, sub):
    # of the form (nume / (sqrt(n) - sub))

    seen_states = set()
    period_values = []

    while True:
        current_state = (nume, sub)
        if current_state in seen_states:
            return period_values
        seen_states.add(current_state)

        # We start with
        #   nume / (sqrt(n) - sub)
        # then convert this to
        #   nume * (sqrt(n) + sub) / (n - sub ** 2)
        # by multiplying top and bottom by (sqrt(n) + sub).

        # This is the value of the denominator after we flip the fraction.
        # We also know that `nume` evenly divides (n - sub ** 2), so we factor
        # that in immediately.
        denom = int((n - sub ** 2) / nume)
        # To compute the next period value, we take the integer portion of this
        # new fraction.
        next_value = int((math.sqrt(n) + sub) / denom)
        period_values.append(next_value)
        # Subtract (next_value * (denom/denom))
        sub = -(sub - denom * next_value)
        nume = denom


def get_partial_values(n):
    first = int(math.sqrt(n))
    period = _find_fraction_period_helper(n, 1, first)
    pvs = itertools.chain([first], itertools.cycle(period))
    return pvs


def gen_convergents(pvs):
    current = next(pvs)
    yield current
    # Lazily recurse in continued fraction form
    fun = lambda x: current + Fraction(1, x)
    yield from map(fun, gen_convergents(pvs))


def solve():
    MAX = 1000
    max_x = (0, 0)
    for d in range(1, MAX + 1):
        if int(math.sqrt(d)) ** 2 == d:
            continue
        for conv in gen_convergents(get_partial_values(d)):
            if conv.numerator ** 2 - d * conv.denominator ** 2 == 1:
                max_x = max(max_x, (conv.numerator, d))
                break
    return max_x[1]


if __name__ == '__main__':
    print('The answer is {}'.format(solve()))
