from euler import slowPrimes, digitize, undigitize

def findTruncatable():
    primeCount = 0
    primeSum = 0

    # Guess at an upper bound
    primeList, primeSieve = slowPrimes(1000000)

    for p in primeList[4:]:
        digits = digitize(p)

        for i in xrange(1, len(digits)):
            num = undigitize(digits[i:])
            if not primeSieve[num]:
                break
            num = undigitize(digits[:-1*i])
            if not primeSieve[num]:
                break
        else:
            primeCount += 1
            primeSum += p
        if primeCount == 11:
            break

    # Check that we reached 11 primes
    print(primeCount)
    return primeSum

print(findTruncatable())
