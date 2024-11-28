#!/usr/bin/python3
'''module for make change'''


def makeChange(coins, total):
    '''
    Given a pile of coins of different values
    returns the fewest number of coins needed to meet a given amount total.
    solved by dp down up approuch
    '''
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for index in range(coin, total + 1):
            dp[index] = min(dp[index], dp[index - coin] + 1)

    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
