# Project Euler (Problem 1)
# Created: 2012-06-11
# Created by: William McDonald

def sum(n):
	flr = 999 / n
	return (n * (flr * (flr + 1)) / 2)

print(sum(3) + sum(5) - sum(15))
