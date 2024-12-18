#!/usr/bin/python3

def sieve_of_eratosthenes(limit):
    """
    Generate a list of primes up to
    `limit` using the Sieve of Eratosthenes.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]


def is_winner(x, nums):
    """
    Determine the winner of the prime game based on
    `x` rounds and `nums` list.
    """
    max_n = max(nums)  # Find the maximum n from all rounds
    # Generate all primes up to the largest `n`
    primes = sieve_of_eratosthenes(max_n)

    # Function to simulate a game for a single round
    def play_game(n):
        """
        Simulate the game for a single round where n is the largest
        number in the set.
        """
        numbers = list(range(1, n + 1))  # Set of numbers from 1 to n
        turn = 0  # Maria starts first (turn 0 for Maria, 1 for Ben)

        while True:
            # Find the smallest prime that is still in the list
            prime_found = False
            for prime in primes:
                if prime <= n and prime in numbers:
                    prime_found = True
                    # Remove the prime and its multiples
                    numbers = [num for num in numbers if num % prime != 0]
                    break

            # If no prime was found, the current player loses
            if not prime_found:
                return 'Ben' if turn == 0 else 'Maria'

            # Switch turns
            turn = 1 - turn

    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
