# Project Euler Problem 28
# Created on: 2012-06-21
# Created by: William McDonald

 total = 1
 for i in range(1001, 1, -2): total += (i * i) * 4 - (i - 1) * 6
 print(total)