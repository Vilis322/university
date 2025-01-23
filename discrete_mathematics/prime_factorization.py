def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []

    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]


def prime_factorization(n):
    primes = sieve_of_eratosthenes(int(n ** 0.5) + 1)
    factors = []

    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime

    if n > 1:
        factors.append(n)

    return factors


print(prime_factorization(120))
