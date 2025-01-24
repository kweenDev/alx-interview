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


def countPrimesUpTo(n):
    """
    Counts the number of prime numbers up to n (inclusive).

    Parameters:
        n (int): The range limit to count primes.

    Returns:
        int: The count of prime numbers between 1 and n.
    """
    count = 0
    for i in range(2, n + 1):
        if isPrime(i):
            count += 1
    return count


def isWinner(x, nums):
    """
    Determines the winner of the "Prime Game" after x rounds.

    Parameters:
        x (int): The number of rounds to be played.
        nums (list of int): A list where each element represents the range of
        numbers for a round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben"),
        or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = countPrimesUpTo(n)
        # Maria wins if the number of primes is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    # Example usage
    x = 3
    nums = [4, 5, 6]
    print(isWinner(x, nums))  # Expected Output: "Maria"
