from euler import slowPrimes, primes
import math

primeList, primeSieve = slowPrimes(100000)

k = 135
while True:
    k += 2
    x = 0
    while k - 2 >= 2 * x * x:
        if primeSieve[k - 2*x*x]:
            break
        x += 1
    else:
        print(k, x)
        break
