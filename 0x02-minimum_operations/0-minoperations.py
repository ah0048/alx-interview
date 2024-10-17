#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''finds the fewest number of operations needed to result in exactly n H'''
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
