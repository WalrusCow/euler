import math

# How many N digit numbers enist of the form a^N, for any a?

def solve():
    total_numbers = 0
    n = 0
    while True:
        n += 1
        upper_bound = 10 ** n - 1
        lower_bound = 10 ** (n - 1)

        lowest_number = math.ceil(lower_bound ** (1 / n))
        highest_number = int(upper_bound ** (1 / n))

        # Account for arithmetic imprecision
        if len(str(highest_number ** n)) > n:
            highest_number -= 1
        if len(str(lowest_number ** n)) < n:
            lowest_number += 1

        if highest_number < lowest_number:
            return total_numbers
        total_numbers += highest_number - lowest_number + 1


if __name__ == '__main__':
    ans = solve()
    print('The answer is {}'.format(ans))
