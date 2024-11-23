def user_input(input_message="message"):
    info = input(f"Please enter {input_message}:\n")
    return info


def main():
    first_name = user_input(input_message="your first name")
    last_name = user_input(input_message="your last name")
    email = user_input(input_message="your email")
    profession = user_input(input_message="your profession")

    full_name = f"{first_name} {last_name} - {email}"
    width = max(len(full_name), len(profession)) + 6
    business_card = [
        "+" + "-" * (width - 2) + "+",
        "|" + " " * (width - 2) + "|",
        "|" + full_name.center(width - 2) + "|",
        "|" + " " * (width - 2) + "|",
        "|" + profession.center(width - 2) + "|",
        "|" + " " * (width - 2) + "|",
        "+" + "-" * (width - 2) + "+"
    ]

    print("\n".join(business_card))


if __name__ == "__main__":
    main()
