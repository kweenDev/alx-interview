#!/usr/bin/python3
"""
Prime Game Module

This module implements the logic for a two-player
game based on prime numbers.
It includes functions to:
1. Generate a list of prime numbers up to a given
limit using the Sieve of Eratosthenes.
2. Simulate the prime game for multiple rounds and
determine the overall winner.

Functions:
- sieve_of_eratosthenes(limit): Generates all prime numbers
up to a given limit.
- is_winner(x, nums): Determines the winner of the game based
on the number of rounds (x) and a list of maximum numbers (nums).

Game Rules:
1. Maria and Ben take turns choosing a prime number from a set
of numbers from 1 to n.
2. The chosen prime and all its multiples are removed from the set.
3. The player unable to make a move loses the round.
4. The player who wins the most rounds out of x rounds is the overall
winner.
"""


def sieve_of_eratosthenes(limit):
    """
    Generate a list of prime numbers up to
    `limit` using the Sieve of Eratosthenes algorithm.

    Parameters:
    limit (int): The upper bound for generating prime numbers.

    Returns:
    list: A list of prime numbers up to the given limit.
    """
    # Create a sieve array initialized to True,
    # assuming all numbers are prime initially
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
    nums (list): A list of integers representing the value of
    `n` for each round.

    Returns:
    str: The name of the player who wins the most rounds ('Maria' or 'Ben').
    If no clear winner, returns None.
    """
    # Find the max value of n from all rounds to limit the
    # sieve of Eratosthenes
    max_n = max(nums)

    # Generate all prime numbers up to the largest `n`
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        """
        Simulate a game for a single round where n is the
        largest number in the set.

        Parameters:
        n (int): The upper limit for the current round of the game.

        Returns:
        str: The name of the player who wins the round ('Maria' or 'Ben').
        """
        numbers = list(range(1, n + 1))  # Set of numbers from 1 to n
        turn = 0  # Maria starts first (turn 0 for Maria, 1 for Ben)

        while True:
            # Flag to track if a prime was found during the round
            prime_found = False

            # Find the smallest prime that is still in the list
            for prime in primes:
                if prime <= n and prime in numbers:
                    prime_found = True
                    # Remove the prime and its multiples from the list
                    numbers = [num for num in numbers if num % prime != 0]
                    break

            # If no prime is found, the current player loses
            if not prime_found:
                return 'Ben' if turn == 0 else 'Maria'

            # Switch turns
            turn = 1 - turn

    # Track wins for Maria and Ben across all rounds
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine and return the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
