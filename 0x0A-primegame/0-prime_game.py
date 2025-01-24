#!/usr/bin/python3
"""
Prime Game Module

This module implements the logic for a two-player game based on prime numbers.
It includes functions to:
1. Generate a list of prime numbers up to a given limit using the Sieve of
Eratosthenes.
2. Simulate the prime game for multiple rounds and determine the overall
winner.

Functions:
- sieve_of_eratosthenes(limit): Generates all prime numbers up to a given
limit.
- is_winner(x, nums): Determines the winner of the game based on the number of
rounds (x) and a list of maximum numbers (nums).
- rm_multiples(ls, x): Removes multiples of a given number from a list.

Game Rules:
1. Maria and Ben take turns choosing a prime number from a set of numbers from
1 to n.
2. The chosen prime and all its multiples are removed from the set.
3. The player unable to make a move loses the round.
4. The player who wins the most rounds out of x rounds is the overall winner.
"""


def sieve_of_eratosthenes(limit):
    """
    Generate a list of prime numbers up to `limit` using the Sieve of
    Eratosthenes algorithm.

    Parameters:
    limit (int): The upper bound for generating prime numbers.

    Returns:
    list: A list of prime numbers up to the given limit.
    """
    # Create a sieve array set to True, assuming all numbers are prime
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Start marking multiples of each prime as False (not prime)
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            # Mark multiples of the current prime as non-prime
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    # Return a list of all prime numbers up to the limit
    return [i for i in range(2, limit + 1) if sieve[i]]


def is_winner(x, nums):
    """
    Determine the winner of the prime game based on `x` rounds and `nums` list.

    Parameters:
    x (int): The number of rounds played.
    nums (list): A list of integers representing the value of `n` for
    each round.

    Returns:
    str: The name of the player who wins the most rounds ('Maria' or 'Ben').
         If there is no winner, returns None.
    """
    # Find the maximum value of n from all rounds to limit the sieve
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize counters for Ben and Maria
    ben = 0
    maria = 0

    # Generate a list of prime numbers up to the maximum value of n
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Simulate the game for each round and count the number of wins
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Remove multiples of a given number from a list.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
