#!/usr/bin/python3
"""
Prime Game Solution
Author: Refiloe Radebe
Date: January 24, 2025
Description: A Python program to determine the winner of a series of rounds in
the "Prime Game".
"""


def isPrime(num):
    """
    Determines if a number is prime.

    Parameters:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generatePrimeCounts(max_num):
    """
    Generates the cumulative count of primes up to each number.

    Parameters:
        max_num (int): The range limit to count primes.

    Returns:
        int: The count of prime numbers between 1 and max_num.
    """
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if isPrime(1) else 0)
    return prime_counts


def isWinner(x, nums):
    """
    Determines the winner of the "Prime Game".

    Parameters:
        x (int): The number of rounds to be played.
        nums (list of int): A list of numbers for each round.

    Returns:
        str: The name of the winner ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_counts = generatePrimeCounts(max_num)

    maria_wins = 0
    ben_wins = 0

    for num in nums[:x]:
        # Determine the number of primes in the current round
        primes_up_to_num = prime_counts[num]

        # If the number of primes is odd, Maria wins the round
        if primes_up_to_num % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
