from problem41Words import *

def computeTris(s, n, cap):
    ''' Add new triangles up to cap to s. s contains triangles up
    number n already.
    Return a tuple (s, i, tri)
    '''
    tri = 0
    i = n
    while tri <= cap:
        i += 1
        tri += i
        s.add(tri)
    return s, i, tri

numTris = 0
OFFSET = ord('A') - 1
tris, n, maxTri = computeTris(set(), 0, 26*18)
for w in words:
    val = sum(ord(c) - OFFSET for c in w)
    if val > maxTri:
        tris, n, maxTri = computeTris(tris, n, val)
    if val in tris:
        numTris += 1
print(numTris)
