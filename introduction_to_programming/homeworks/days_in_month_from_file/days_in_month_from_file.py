from datetime import datetime as dt
from pathlib import Path


class MyError(Exception):
    def __init__(self, text):
        super().__init__(text)


def user_input(input_message):
    return input(input_message).strip().lower()


def is_valid_date(string):
    try:
        dt.strptime(string, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def get_num_of_month(date_string):
    return int(date_string.split(".")[1])


def get_days_in_month(file, list_of_days):
    dates = Path(file).read_text()

    for line in dates.splitlines():
        if is_valid_date(line):
            month = get_num_of_month(line)
            print(f"Number of days in {line} is {list_of_days[month - 1]}")


def main():
    file_name = user_input("Enter a file name: ")
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        if not file_name.endswith("dates.txt"):
            raise MyError("Entered an invalid file name!")

        get_days_in_month(file_name, days_in_month)
    except MyError as e:
        print(str(e))


if __name__ == "__main__":
    main()
