def num_of_days(num_of_month, year):
    dictionary_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if 1 <= num_of_month <= 12:
        days = dictionary_of_month[num_of_month]
        if is_leap_year(year):
            return f"In this month will be {days+1} days (this is a leap year)." if num_of_month == 2 \
                                                    else f"In this month will be {days} days (this is a leap year)."

        else:
            return f"In this month will be {days} days (this is a common year)."


def is_leap_year(year):
    return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False


def user_input():
    while True:
        try:
            user_input_month = input("Enter the number of a month: ")
            user_input_month = int(user_input_month)
            if user_input_month in range(1, 13):
                user_input_year = input("Enter the year: ")
                user_input_year = int(user_input_year)
                return user_input_month, user_input_year
            else:
                print("The number of a month must be in the range [1-12].")
                continue
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue


if __name__ == "__main__":
    month, year = user_input()
    print(num_of_days(month, year))
