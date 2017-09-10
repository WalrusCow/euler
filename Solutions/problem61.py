from collections import defaultdict


def triangle(n):
    return int((n * (n + 1)) / 2)


def square(n):
    return n * n


def pentagon(n):
    return int((n * (3 * n - 1)) / 2)


def hexagon(n):
    return n * (2 * n - 1)


def heptagon(n):
    return int((n * (5 * n - 3)) / 2)


def octagon(n):
    return n * (3 * n - 2)


def find_values_for_digits(first_two, poly_values):
    return {poly_num: {last_two for last_two in val_map[first_two]}
            for poly_num, val_map in poly_values}


def find_longest_sequence(poly_values, sequence):
    if not poly_values:
        if sequence[-1] % 100 == sequence[0] // 100:
            return sequence
        else:
            # The ends don't match -- remove the last one :)
            return sequence[:-1]

    best_sequence = sequence

    first_two = sequence[-1] % 100
    for poly_num, digit_map in poly_values.items():
        for last_two in digit_map[first_two]:
            new_sequence = find_longest_sequence(
                {p: dm for p, dm in poly_values.items() if p != poly_num},
                sequence + [first_two * 100 + last_two],
            )
            if len(new_sequence) > len(best_sequence):
                best_sequence = new_sequence
    return best_sequence


if __name__ == '__main__':
    poly_funs = [triangle, square, pentagon, hexagon, heptagon, octagon]
    poly_values = defaultdict(lambda: defaultdict(set))
    for poly_num, poly_fun in enumerate(poly_funs, start=3):
        for n in range(1, 10000):
            val = poly_fun(n)
            if val >= 10000:
                break
            elif val >= 1000:
                poly_values[poly_num][val // 100].add(val % 100)

    for first_two, last_twos in poly_values.pop(3).items():
        for last_two in last_twos:
            sequence = find_longest_sequence(
                poly_values,
                [first_two * 100 + last_two],
            )
            if len(sequence) == 6:
                print('Sequence: {}'.format(', '.join(map(str, sequence))))
                print('Sum is {}'.format(sum(sequence)))
