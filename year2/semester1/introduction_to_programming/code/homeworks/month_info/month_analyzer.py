class NumOfMonth:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.num_of_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        self.name_of_month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
                                   8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    def get_num_of_month(self):
        if self.month == 2 and self.is_leap_year():
            return self.num_of_month_dict[self.month] + 1

        return self.num_of_month_dict[self.month]

    def get_name_of_month(self):
        return self.name_of_month_dict[self.month]

    def get_year(self):
        leap_message = "a leap year" if self.is_leap_year() else "not a leap year"
        return f"{self.year} is {leap_message}"

    def is_valid_month(self):
        return self.month in self.num_of_month_dict

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
