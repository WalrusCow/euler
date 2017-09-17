import math

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


def find_fraction_period(n):
    return _find_fraction_period_helper(n, 1, int(math.sqrt(n)))


def solve():
    MAX = 10000
    num_odd_periods = 0
    for x in range(1, MAX + 1):
        if int(math.sqrt(x)) ** 2 != x:
            period = find_fraction_period(x)
            if len(period) % 2 == 1:
                num_odd_periods += 1
    return num_odd_periods


if __name__ == '__main__':
    print('The answer is {}'.format(solve()))
