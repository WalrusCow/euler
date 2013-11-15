from euler import digitize, permuteInts, undigitize

# 0 to 9
DIGITS = set(xrange(10))

def compute(nums, digitList, digitSet, answerList):
    ''' Recursively find the answer. '''

    # Should be at a base case
    if not nums:
        if len(digitList) != 9: return
        answer = undigitize(list(DIGITS.difference(digitSet)) + digitList)
        answerList.append(answer)
        return

    checkNum = nums[-1]
    numStart = digitList[-2:] + ['']

    # Make the digits to check
    digitsToCheck = DIGITS.difference(digitSet)

    # Check all possible digits
    for newDigit in digitsToCheck:
        numStart[-1] = newDigit
        if undigitize(numStart) % checkNum: continue

        # Add to the digit list and digit set
        newDigitList = digitList + [newDigit]
        newDigitSet = digitSet.union(set((newDigit,)))

        # Recursively call compute
        compute(nums[:-1], newDigitList, newDigitSet, answerList)

def getAnswer():
    answerList = []

    for n in xrange(10, 1000, 2):
        d = digitize(n)
        if n < 100:
            d.insert(0, 0)
        sd = set(d)
        if len(d) != len(sd):
            continue
        compute([17, 13, 11, 7, 5, 3], d, sd, answerList)

    return sum(answerList)

print(getAnswer())
