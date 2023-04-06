#!/usr/bin/python3
"""
primegame
"""


def prime(n):
    """
    return prime numbers between 1-n
    """
    num = []
    pr = [True] * (n + 1)
    for a in range(2, n + 1):
        if (pr[a]):
            num.append(a)
            for b in range(a, n + 1, a):
                pr[b] = False
    return num


def isWinner(x, nums):
    """
    winner
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for b in range(x):
        num = prime(nums[b])
        if len(num) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None