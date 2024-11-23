def user_input(input_message="message", error_message="error message", is_number=False):
    while True:
        user_input = input(f"Please, enter {input_message}:\n")

        if is_number:

            try:

                user_input = int(user_input)

                if user_input <= 0:
                    print("The number of sentence repetitions cannot be negative or equal to 0!\n")

                return user_input

            except ValueError:
                print(f"Invalid input! {error_message}\nPlease, enter the value again!\n")
        else:
            return user_input


def main():
    sentence = user_input(input_message="a sentence to be repeated in his mantra", is_number=False)
    times_to_repeat = user_input(input_message="how many times the mantra is to be repeated",
                                 error_message="The program expects numeric input!", is_number=True)

    for i in range(times_to_repeat):
        print(sentence)


if __name__ == "__main__":
    main()
