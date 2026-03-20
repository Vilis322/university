def user_input(input_message="message"):
    while True:
        number = input(input_message)

        if number.lower().strip() == "done":
            print("You decided to stop the program.")
            return number.lower().strip()
        try:
            number = int(number)
            return number
        except ValueError:
            print("The program expect from you a number!")


def make_list():
    min_max_square_sum_list = []
    while True:
        number = user_input("\nPlease enter a number or 'done' if you don't want to write a numbers anymore: ")
        if number == "done":
            return min_max_square_sum_list

        min_max_square_sum_list.append(number)


def main():
    list_of_numbers = make_list()

    if not list_of_numbers:
        return "The list is empty!"

    list_of_squares = sorted([number ** 2 for number in list_of_numbers])
    list_of_evens = [number for number in list_of_numbers if number % 2 == 0]
    count_of_even = len(list_of_evens)
    max_number = max(list_of_numbers)
    min_number = min(list_of_numbers)
    sum_of_numbers = sum(list_of_numbers)

    print(f"\nMaximum: {max_number} \nMinimum: {min_number}\nSum: {sum_of_numbers}\nSquares: {list_of_squares}")
    print(f"Count of evens: {count_of_even}")


if __name__ == "__main__":
    print(main())
