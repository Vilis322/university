def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def main():
    a = 236236346342632632
    b = 12523425645364364356
    greatest_common_divisor = gcd(a, b)
    least_common_multiple = lcm(a, b)
    print(f"НОД({a}, {b}) = {greatest_common_divisor}")
    print(f"НОК({a}, {b}) = {least_common_multiple}")


if __name__ == "__main__":
    main()
