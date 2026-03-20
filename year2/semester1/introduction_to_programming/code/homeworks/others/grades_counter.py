class InvalidInput(Exception):
    pass


def user_input(input_message="message"):
    value = input(input_message)
    return value


def main():
    first_name = user_input("\nPlease enter your first name: ").strip().capitalize()
    last_name = user_input("\nPlease enter your last name: ").strip().capitalize()

    while True:
        try:
            grades = user_input("\nPlease enter your grades in range from A to E: ").replace(" ", "").upper()
            if not all(grade in ["A", "B", "C", "D", "E"] for grade in list(grades)):
                raise InvalidInput("\nInvalid grades entered!")
            break

        except InvalidInput as e:
            print(str(e))
            print("\nThe grades must be between A and E!\nPlease try again!")

    all_grades = len(grades)
    grades_a_and_b = sum(1 for grade in grades if grade in ["A", "B"])
    second_grade = grades[1] if len(grades) > 1 else "N/A"
    print(f"Hello, {first_name} {last_name}!"
          f"\nYour grades are {grades}."
          f"\nYou have {all_grades} grades."
          f"\nYour grade for the second course is {second_grade}"
          f"\nThe number of A's and B's is {grades_a_and_b}.")


if __name__ == "__main__":
    main()
