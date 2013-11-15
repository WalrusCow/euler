from euler import primes, digitize, undigitize

def findCircular(n):
    ''' Find all circular primes below n. '''

    primeList, primeSieve = primes(n)
    # 2 and 5 will be skipped
    circleCount = 2

    for p in primeList:
        # If any even nums then at least 1 permutation cannot be prime
        if any(n % 2 == 0  or n == 5 for n in digitize(p)):
            continue
        if all(primeSieve[(r - 3) / 2] for r in rotate(p)):
            circleCount += 1

    return circleCount

def rotate(n):
    ''' Rotate the number n.
    e.g. 123 -> 123, 231, 312
    This is a generator.
    '''
    digitList = digitize(n)
    for i in xrange(len(digitList)):
        yield undigitize(digitList[i:] + digitList[:i])

print(findCircular(1000000))
