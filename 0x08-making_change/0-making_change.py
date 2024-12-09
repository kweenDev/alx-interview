#!/usr/bin/python3
"""
0-making_change.py

This module contains the function `makeChange`, which determines the fewest
number of coins needed to make up a given total amount from a list of coin
denominations.

Author: Refiloe Radebe
Date Created: December 9, 2024
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The target amount to achieve with the coins.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it
        is not possible to achieve the total with the given denominations.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a greedy approach
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if total <= 0:
            break
        # Use as many of the current coin as possible
        num_coins = total // coin
        coin_count += num_coins
        total -= num_coins * coin

    return coin_count if total == 0 else -1
