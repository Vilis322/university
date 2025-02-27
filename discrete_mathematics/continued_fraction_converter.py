def rational_to_continued_fraction(a, b):
    continued_fraction = []
    while b != 0:
        quotient = a // b
        continued_fraction.append(quotient)
        a, b = b, a % b

    return continued_fraction


def main():
    numerator = 1241
    denominator = 10
    result = rational_to_continued_fraction(numerator, denominator)
    print(f"Цепная дробь для {numerator}/{denominator}: {result}")


if __name__ == "__main__":
    main()
