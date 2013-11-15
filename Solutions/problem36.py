from euler import digitize, undigitize

def isPalindrome(li):
    ''' Determine if a list is a palindrome. '''

    # We don't need to check the middle elem
    l = len(li)
    for i in xrange(l / 2):
        if li[i] != li[l - 1 - i]:
            return False
    return True

def dblPal():
    ''' Find sum of all double palindromes (base 2 and 10) below 1000000. '''

    palSum = 0

    # Also do the 1 digit numbers
    for num in xrange(1, 10, 2):
        if isPalindrome(bin(num)[2:]):
            palSum += num

    # All palindromes that are 2, 3, 4, 5 digits in length
    for x in xrange(1, 100):
        digits = digitize(x)
        if digits[0] % 2 == 0: continue
        endDigits = digits[::-1]
        num = undigitize(digits + endDigits)

        if isPalindrome(bin(num)[2:]):
            palSum += num

        for d in xrange(10):
            num = undigitize(digits + [d] + endDigits)
            if isPalindrome(bin(num)[2:]):
                palSum += num

    # Also do the 6 digit numbers
    for x in xrange(100, 1000):
        digits = digitize(x)
        if digits[0] % 2 == 0: continue
        endDigits = digits[::-1]
        num = undigitize(digits + endDigits)

        if isPalindrome(bin(num)[2:]):
            palSum += num

    return palSum

print(dblPal())
