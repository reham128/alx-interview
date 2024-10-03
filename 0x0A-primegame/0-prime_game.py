#!/usr/bin/python3
"""where x is the number of rounds and nums is an array of n"""


def sieve_of_eratosthenes(max_n):
    """Returns a list of prime numbers up to max_n."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x < 1:
        return None
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes_set = set(primes)
        primes_set = {p for p in primes_set if p <= n}
        turn = 0
        while primes_set:
            prime = min(primes_set)
            primes_set = {p for p in primes_set if p % prime != 0}
            turn = 1 - turn
        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
