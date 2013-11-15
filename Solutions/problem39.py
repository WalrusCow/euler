# if a + b + c = P then we need a + b > c with c hypotenuse
# we can also say that a <= b
# Then we also need a^2 + b^2 = c^2

# We can start at 501 since all less than 501 will have a multiple
# less than 1000

def findTris(p):
    ''' Find potential triangle sides of perimeter p.
    yield (a,b,c)
    '''
    maxC = p / 2
    n = 0
    for c in xrange(maxC, 1, -1):
        maxA = (p - c) / 2
        for a in xrange(1, maxA+1):
            b = p-c-a
            if a*a + b*b == c*c:
                n += 1
    return n

def findMaxTris(cap):
    maxTris = 1
    maxP = 0
    for p in xrange(cap, (cap+1)/2, -2):
        n = findTris(p)
        if n > maxTris:
            maxP = p
            maxTris = n
    return maxP

print(findMaxTris(1000))
