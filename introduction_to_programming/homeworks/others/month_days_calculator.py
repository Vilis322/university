def num_of_days(num_of_month):
    dictionary_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    while num_of_month not in dictionary_of_month:
        try:
            num_of_month = int(num_of_month)
            if num_of_month in dictionary_of_month:
                return f"In this month will be {dictionary_of_month[num_of_month]} days."
            else:
                print("The number of a month must be in the range [1-12]")
                num_of_month = input("Please enter valid number: ")
        except ValueError:
            num_of_month = input("Invalid input. Please enter a number: ")


user_input_month = input("Enter the number of a month: ")
print(num_of_days(user_input_month))
