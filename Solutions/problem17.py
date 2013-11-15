# Project Euler Problem 17
# Created on: 2012-06-18
# Created by: William McDonald

ones = ["one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]
ones = sum(map(len, ones))

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
teens = sum(map(len, teens))

tens = ["twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"]
tens = sum(map(len, tens))

hundred = len("hundred")
thousand = len("thousand")

# ones = 9 times each per hundred = 90 times each
# teens = 1 time each per hundred = 10 times each
# tens = 10 times each per hundred = 100 times each
# and = 99 times per hundred (9 hundred) = 891 times
# ones = 100 times each in front of hundred
# hundred = 900 times
# thousand = 1 time

print(ones*90 + teens*10 + tens*100 + 3*(99*9) + ones*100 + hundred*900 + thousand + 3)
