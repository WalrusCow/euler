def findSum(left, coins):
    if not left or not coins:
        return 1
    coin = coins[0]
    coins = coins[1:]
    return sum(findSum(left - v, coins) for v in range(0, left + 1, coin))

coins = (200, 100, 50, 20, 10, 5, 2)
print(findSum(200, coins))
