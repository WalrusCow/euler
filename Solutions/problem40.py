from euler import digitize

def getDigit(n):
    ''' Retrieve the nth digit from Champernowe's constant. '''
    digits = 1
    while True:
        if getDigit.numDigits[digits-1] > n:
            break
        n -= getDigit.numDigits[digits-1]
        digits += 1
    pwr = 10**(digits-1)
    n -= 1
    # n is now the number of digits into this we go
    # Find what number after the power of 10 n belongs to
    num = n / digits
    num += pwr
    return digitize(num)[n % digits]

getDigit.numDigits = []
for n in xrange(1, 7):
    getDigit.numDigits.append(9 * (10**(n-1)) * n)

print(reduce(lambda x,y: x*y, (getDigit(10**i) for i in xrange(7)), 1))
