#!/usr/bin/python3
"""
Minimum Operations to achieve n characters using Copy All and Paste
Author: KweenDev (Refiloe Radebe)
Date: 2024-10-16
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize n, adding the divisors to the operation count
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
