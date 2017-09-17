from fractions import Fraction

def _e_partial_value_at_idx(idx):
    return 2 if idx == 0 else 2 * (idx // 3 + 1) if idx % 3 == 2 else 1


class EPartialValueIterator:
    def __init__(self, start=0, stop=None, step=1):
        self._index = start or 0
        self._stop = stop
        self._step = step or 1


    def _should_stop(self):
        if self._step < 0:
            if self._index < 0:
                return True
            if self._stop is not None:
                return self._index <= self._stop
        elif self._stop is not None:
            return self._index >= self._stop


    def __iter__(self):
        while not self._should_stop():
            yield _e_partial_value_at_idx(self._index)
            self._index += self._step


class MetaEPartialValues(type):
    def __iter__(self):
        yield from EPartialValueIterator()


    def __getitem__(self, val):
        if type(val) == int:
            return _e_partial_value_at_idx(val)
        return EPartialValueIterator(val.start, val.stop, val.step)


class EPartialValues(metaclass=MetaEPartialValues):
    pass


# Get the sum of the digits in the 100th convergent of e (100 terms of
# continued fraction)
def solve():
    answer = Fraction(EPartialValues[99])
    for pv in EPartialValues[98::-1]:
        answer = pv + (1 / answer)
    return sum(map(int, str(answer.numerator)))


if __name__ == '__main__':
    print('The answer is {}'.format(solve()))
