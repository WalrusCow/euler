# Project Euler (Problem 2)
# Created: 2012-06-11
# Created by: William McDonald

def fibEven(n):
	sum = 0
	current = 2
	previous = 1
	while current <= n:
		nxt = current + previous
		nextEven = ((current + previous) * 2) + current

		print(previous)
		print(current)

		sum += current
		current, previous = nextEven, (nxt + current)

	else:
		print(sum)

fibEven(4000000)
