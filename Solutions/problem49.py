from collections import defaultdict
from euler import slowPrimes, digitize, undigitize

primeList, primeSieve = slowPrimes(10000)

def makeCandidates(lst, sieve):
    ''' Make a list of candidates for this problem. '''
    primeSet = set()
    for p in lst:
        digits = digitize(p)
        if len(digits) != 4: continue
        # Check if at least 3 permutations give primes and add the maximum
        # value from the permutations to the candidates
        count = 0
        m = 0
        for perm in permuteInts(digits):
            if perm > 1000 and primeSieve[perm]:
                count += 1
                m = max(perm, m)
        if count >= 3:
            primeSet.add(m)

    permList = []
    for p in primeSet:
        tmpLst = []
        for perm in permuteInts(digitize(p)):
            if primeSieve[perm] and perm > 1000:
                tmpLst.append(perm)
        permList.append(sorted(tmpLst))

    return permList

def permuteInts(L):
    ''' Permute a list of digits into integers. '''
    previous = set()
    def _permute(lst, acc):
        if not lst:
            yield acc
        for i, c in enumerate(lst):
            for perm in _permute(lst[:i] + lst[i+1:], acc*10 + c):
                if perm not in previous:
                    yield perm
                    previous.add(perm)
    return _permute(L, 0)

def findDifferences(lop):
    ''' Compute the number of each difference in each thing. '''

    diffList = []
    for permList in lop:
        countDict = defaultdict(int)

        # Check each larger prime and record the difference between
        # this one and that one
        for i, p in enumerate(permList):
            for bp in permList[i+1:]:
                if bp - p == 3330:
                    countDict[bp - p] += 1

        countDict = {k: v for k, v in countDict.iteritems() if v >= 2}
        diffList.append(countDict)

    return diffList

a = sorted(makeCandidates(primeList, primeSieve), key=lambda x:x[0])
for i, x in enumerate(findDifferences(a)):
    if x: print(a[i], x)
