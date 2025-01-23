import math


def is_prime_fermat(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    a = math.ceil(math.sqrt(n))
    while a**2 - n < n:
        b_squared = a**2 - n
        b = math.isqrt(b_squared)
        if b * b == b_squared:
            return False
        a += 1

    return True


print(is_prime_fermat(29))
print(is_prime_fermat(30))
print(is_prime_fermat(2))
print(is_prime_fermat(1))
print(is_prime_fermat(293))
