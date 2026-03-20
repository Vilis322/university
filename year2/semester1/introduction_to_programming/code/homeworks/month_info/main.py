from month_analyzer import NumOfMonth


def user_input(input_message="message"):
    while True:
        value = input(input_message).lower().strip()
        if value == "done":
            print("\nYou decided to stop the program.")
            exit()

        try:
            return int(value)
        except ValueError as e:
            print(str(e))
            print("\nInvalid input!\nPlease try again!")


def main():
    while True:
        month = user_input("\nEnter a number of month or 'done' to stop the program: ")
        number_of_month = NumOfMonth(month, None)

        if not number_of_month.is_valid_month():
            print("\nInvalid input!\nNumber of month must be in range from 1 to 12!\nPlease, try again!")
            continue

        year = user_input("\nEnter a year or 'done' to stop the program: ")
        number_of_month.year = year
        print(f"\nIn this month {number_of_month.get_num_of_month()} days."
              f"\nThe name of month is {number_of_month.get_name_of_month()}."
              f"\nThe year {number_of_month.get_year()}.")


if __name__ == "__main__":
    main()
