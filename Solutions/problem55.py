import euler

def isPalindrome(n):
    ''' Determine if n is a palindrome. '''
    digits = euler.digitize(n)
    return euler.isPalindrome(digits)

def isLychrel(n):
    ''' Determine if n is a "Lychrel" number. '''
    for _ in range(0, 50):
        digits = euler.digitize(n)
        revN = euler.undigitize(digits[::-1])

        n = revN + n
        if isPalindrome(n):
            return False

    return True

def lychrel(n):
    ''' Find all "Lychrel" numbers under n. '''

    # True if Lychrel
    lychrels = [False] * (n-1)
    for i in range(1, n):
        if isLychrel(i):
            lychrels[i - 1] = True

    return sum(lychrels)

if __name__ == '__main__':
    print(lychrel(10000))
