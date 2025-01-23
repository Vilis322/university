import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


print(is_prime(29))
print(is_prime(30))
print(is_prime(2))
print(is_prime(1))
print(is_prime(293))
