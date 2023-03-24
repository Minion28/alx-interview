#!/usr/bin/python3
"""
making_change
"""


def makeChange(coins, total):
    """
    return 0 if total=0, else -1
    """
    if total <= 0:
        return 0

    n = [total + 1] * (total + 1)

    n[0] = 0

    for amt in range(1, total + 1):

        for coin in coins:
            if amt - coin >= 0:
                n[amt] = min(n[amt], 1 + n[amt - coin])
    return n[total] if n[total] != total + 1 else -1
