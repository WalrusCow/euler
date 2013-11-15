from euler import primes

# Computed answer for 100000 and number of primes is 183
PRIME_CAP = 1000000

# Compute all primes below the cap
primeList, _ = primes(PRIME_CAP)

def solve():
    # Idea: For each prime, check for consecutive sequences
    # of primes that sum to it
    answer = 0
    maxConsec = 0
    for prime in reversed(primeList):
        consec = 0 # Number of consecutive primes
        pSum = 0 # Sum so far
        start = 0 # Start index of the sum
        for i, p in enumerate(primeList):
            if p * (maxConsec - consec) >= prime: break
            pSum += p
            consec += 1
            while pSum > prime:
                pSum -= primeList[start]
                start += 1
                consec -= 1
            if pSum == prime:
                if consec > maxConsec:
                    maxConsec = consec
                    answer = prime
                break
    return answer, maxConsec
print(solve())
