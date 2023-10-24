#!/usr/bin/python3
"""0-prime_game module"""


def generate_prime_nums(n):
    """Generates a list of prime numbers"""
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            primes.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False

    return primes


def isWinner(x, nums):
    """Determines the winner of the Prime Game"""
    if not nums or x == 0:
        return None

    maria = ben = 0

    for i in range(x):
        prime = generate_prime_nums(nums[i])
        if len(prime) % 2 == 0:
            ben += 1
        else:
            maria += 1

    return 'Maria' if maria > ben else 'Ben' if ben > maria else None
