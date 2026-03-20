def user_input():
    try:
        cents = input("Please enter a count of cents:\n")
        cents = float(cents)

        if cents <= 0:
            raise ValueError("Your count of cents cannot be a negative or equal 0!")

        return cents
    except ValueError as e:
        print(e)


def converts_cents_to_euro(cents):
    euros = cents // 100
    remaining_cents = cents % 100
    return euros, remaining_cents


def main():
    cents = user_input()
    euros, remaining_cents = converts_cents_to_euro(cents)
    euros, remaining_cents = int(euros), int(remaining_cents)

    if euros > 0:
        if remaining_cents > 0:
            print(f"You have {euros} euros and {remaining_cents} cents.")
        else:
            print(f"You have {euros} euros.")
    else:
        print(f"You have {remaining_cents} cents.")


if __name__ == "__main__":
    main()
