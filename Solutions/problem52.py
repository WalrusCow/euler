from collections import Counter
from euler import digitize, undigitize

n = 100
while True:
    digits = digitize(n)
    digits.insert(0, 1)
    dCount = Counter(digits)
    newNum = undigitize(digits)
    for i in xrange(2, 7):
        if Counter(digitize(newNum*i)) != dCount:
            break
    else:
        print(newNum)
        break
    n += 1
