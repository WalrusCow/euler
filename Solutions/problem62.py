import sys

from collections import defaultdict

class Cube:
    def __init__(self, n):
        self.value = n * n * n
        self.digits = tuple(sorted(str(self.value)))


class MinCounter:
    def __init__(self, cube=None):
        self.value = cube.value if cube is not None else None
        self.count = 0 if cube is None else 1

    def __iadd__(self, other):
        self.count += other.count
        if other.value is not None:
            self.value = other.value if self.value is None else min(self.value, other.value)
        return self


def solve():
    digit_dict = defaultdict(MinCounter)

    n = 0
    current_length = len(str(n * n))
    candidates = []
    while True:
        n += 1

        cube = Cube(n)
        if len(cube.digits) > current_length:
            current_length = len(cube.digits)
            l = [c for c in candidates if c.count == 5]
            if l: return min(c.value for c in l)
            candidates = []

        digit_dict[cube.digits] += MinCounter(cube)
        if digit_dict[cube.digits].count == 5:
            candidates.append(digit_dict[cube.digits])


if __name__ == '__main__':
    ans = solve()
    print('The answer is {}'.format(ans))
