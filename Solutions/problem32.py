def splitString(s, i):
    return s[:i], s[i:]

def permute(it):
    def _permute(aSet, acc):
        if not aSet:
            yield acc
        for c in aSet:
            for perm in _permute(aSet.difference(c), acc + c):
                yield perm
    return _permute(set(it), '')

def products():
    digits = '123456789'
    productSet = set()
    for perm in permute(digits):
        left, product = splitString(perm, 5)
        product = int(product)
        # Need either (1,4) or (2,3) split
        for i in range(1, 3):
            m1, m2 = splitString(left, i)
            if int(m1) * int(m2) == product:
                productSet.add(product)
    return sum(productSet)

print(products())
