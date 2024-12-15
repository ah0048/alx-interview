#!/usr/bin/python3
'''function module'''


def isWinner(x, nums):
    '''determine who the winner of each game is.'''

    Maria_wins = 0
    Ben_wins = 0

    for round in range(x):

        prime = [True for _ in range(nums[round] + 1)]
        prime_nums_count = 0
        p = 2

        while p * p <= nums[round]:
            if prime[p] is True:
                for i in range(p * p, nums[round] + 1, p):
                    prime[i] = False
            p += 1

        for p in range(2, nums[round] + 1):
            if prime[p] is True:
                prime_nums_count += 1

        if prime_nums_count % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if Maria_wins == Ben_wins:
        return None
    elif Maria_wins > Ben_wins:
        return "Maria"
    else:
        return "Ben"
