from birthday_days import BirthdayCounter


def main():
    birthdays = BirthdayCounter("birthday_dates.txt")
    birthdays.printing_instructions()
    user_input = ''

    while user_input != 'exit':
        user_input = input("\nWhat is your choice?\n").lower().strip()

        if user_input == 'list':
            birthdays.get_birthdays_and_people()

        elif user_input in ('1', '2', '3', '4', '5', '6', '7'):
            birthdays.get_weekday_name(user_input)

        elif user_input == 'exit':
            print("\nYou chose to exit from the program. Goodbye!")
            exit()

        else:
            birthdays.get_weekday_name(user_input)


if __name__ == "__main__":
    main()
