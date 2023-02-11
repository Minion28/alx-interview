#!/usr/bin/python3
"""
    method that calculates the fewest no of operations
"""


def minOperations(n: int) -> int:
    """
    return integer
    """
    count = 0

    if n <= 1:
        return count

    for i in range(2, n + 1):
        while (0 == n % i):
            count = count + i
            n = n / i
            if n < i:
                break
    return count
