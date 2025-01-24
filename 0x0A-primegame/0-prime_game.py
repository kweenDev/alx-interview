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
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def rm_multiples(ls, x):
    """
    Remove multiples of a given number from a list.

    Parameters:
    ls (list): A list representing the number set.
    x (int): The number to whose multiples will be removed.

    Returns:
    None: Modifies the list in place.
    """
    for i in range(x * 2, len(ls), x):
        ls[i] = 0


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
    if x <= 0 or not nums:
        return None

    # Find the maximum value in nums to limit the sieve
    max_num = max(nums)

    # Generate a sieve up to the largest number in nums
    sieve = [1] * (max_num + 1)
    sieve[0], sieve[1] = 0, 0  # 0 and 1 are not primes
    for i in range(2, len(sieve)):
        if sieve[i] == 1:
            rm_multiples(sieve, i)

    # Count wins for Maria and Ben
    maria_wins, ben_wins = 0, 0

    for n in nums:
        prime_count = sum(sieve[:n + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
