from datetime import datetime as dt
from pathlib import Path
from time import sleep
from collections import OrderedDict
import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M'
)


class BirthdayCounter:
    def __init__(self, file):
        self.file: str = file
        self.birthdays_and_people: dict = {}
        self.name_of_day = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        self.create_dict_birthdays_and_people()

    def create_dict_birthdays_and_people(self):
        try:
            file_path = Path(self.file)
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            return

        with file_path.open(encoding='utf-8') as f:
            for line_number, birthday in enumerate(f, 1):
                try:
                    birthday = birthday.strip()
                    birthday = dt.strptime(birthday, '%Y-%m-%d')
                    name_of_day = self.name_of_day[dt.weekday(birthday)]
                    self.birthdays_and_people[name_of_day] = self.birthdays_and_people.get(name_of_day, 0) + 1
                except ValueError as e:
                    logging.error(f"Incorrect date format in text file in string {line_number}: {e}")

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.birthdays_and_people = OrderedDict(
            sorted(self.birthdays_and_people.items(), key=lambda item: days_of_week.index(item[0]))
        )

    def get_birthdays_and_people(self):
        for day, value in self.birthdays_and_people.items():
            print(f"In {day} w{'ere' if value > 1 else 'as'} born {value} people.")
            sleep(2)

    def get_weekday_name(self, user_input):
        try:
            user_input = int(user_input.strip())
            key = list(self.birthdays_and_people.keys())[user_input-1]
            print(f"For index {user_input} weekday name is {key}")
        except IndexError as e:
            print(f"Incorrect index input for a weekday name. Please try again!")
            logging.error(f"Incorrect index input for a weekday name: {e}")
        except ValueError as e:
            print(f"Incorrect input for the program. Please try again!")
            logging.error(f"Incorrect input for the program: {e}")

    @staticmethod
    def printing_instructions():
        print("Welcome to the Birthday counter program!")
        sleep(2)
        print("There is a list of dates in the text file, and each of them is a someone's Birthday.")
        sleep(2)
        print("Enter 'list' if you want to see an amount of people who was born in each weekday.")
        sleep(2)
        print("Enter any number from 1 to 7 to see which weekday it is. (for example: enter '1' for 'Monday')")
        sleep(2)
        print("Enter 'exit' to stop running the program.")
        sleep(2)

