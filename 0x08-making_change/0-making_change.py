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
    dict_values = {i: total + 1 for i in range(total + 1)}
    dict_values[0] = 0
    for key, value in dict_values.items():
        for coin in coins:
            if coin > key:
                continue
            prev_key = key - coin
            value = min(dict_values[prev_key] + 1, value)
            dict_values[key] = value

    if dict_values[total] != total + 1:
        return dict_values[total]
    else:
        return -1
