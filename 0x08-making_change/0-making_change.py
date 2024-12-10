#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    n = len(coins)
    result = 0

    for i in range(n):
        if total <= 0:
            break
        result += total // coins[i]
        total %= coins[i]

    return result if total == 0 else -1
