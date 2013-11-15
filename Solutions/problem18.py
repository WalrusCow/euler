'''
Project Euler Problem 18
Created: 2012-06-18
Author: William McDonald
'''

'''
IDEA:
For a given row, store the maximum sum to get to each element in that row by
using the maximum sums for the row above it.

e.g.
      08
    01 02
   01 05 04
==>
    09 10
   01 04 05
==>
   10 15 14

Now simply take the maximum.
'''

FILE_NAME = 'problem18.txt'

def importTri():
    # Import the triangle (convert to ints)
    with open(FILE_NAME) as f:
        return [[int(x) for x in line.split()] for line in f]

def getMax(lastMax, cur):
    # lastMax is a list of maximum sums to elements in the previous rows
    # Add first elements
    newMax = [lastMax[0] + cur[0]]
    for i, n in enumerate(cur[1:-1]):
        newMax.append(max(lastMax[i], lastMax[i+1]) + n)
    # Add last elements
    newMax.append(lastMax[-1] + cur[-1])
    return newMax

def getAns():
    t = importTri()
    # Initially check last maximum
    lastMax = t[0]
    for row in t[1:]: lastMax = getMax(lastMax, row)
    return max(lastMax)

print(getAns())
