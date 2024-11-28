#!/usr/bin/python3
'''module for make change'''


def greedy_sol(coins, total):
    '''
    Given a pile of coins of different values
    returns the fewest number of coins needed to meet a given amount total.
    solved by greedy approuch
    '''
    count = 0
    coins.sort(reverse=True)

    for coin in coins:
        count += total // coin
        total %= coin

    return count if total == 0 else -1


def dp_sol(coins, total):
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


def makeChange(coins, total):
    '''
    Given a pile of coins of different values
    returns the fewest number of coins needed to meet a given amount total.
    '''

    if total <= 0:
        return 0

    greedy_result = greedy_sol(coins, total)
    # if greedy_result != -1:
    #     return greedy_result
    return greedy_result
    # return dp_sol(coins, total)
