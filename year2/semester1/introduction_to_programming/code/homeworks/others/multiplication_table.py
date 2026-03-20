def user_input():

    while True:
        try:
            number = input("Enter a number in range from 1 to 9: ")
            number = int(number)
            if number < 1 or number > 9:
                raise ValueError("\nThe number must be in range from 1 to 9!")

            return number
        except ValueError as e:
            print(str(e))
            print("Invalid input!\nThe program expect an integer in range from 1 to 9!\n")


def multiplication_table(number):
    for i in range(1, 10):
        result = number * i
        print(f"{number} * {i} = {result}")


multiplication_table(user_input())
