#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''finds the fewest number of operations needed to result in exactly n H'''
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            n /= factor
            operations += factor
        else:
            factor += 1

    return operations
