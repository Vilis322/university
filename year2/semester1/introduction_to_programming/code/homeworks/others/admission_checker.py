def pass_mark(student_mark):
    try:
        student_mark = int(student_mark)
        return (
            "The obtained points are enough to be considered for admission."
            if 66 <= student_mark <= 100 else
            "The obtained points are not enough to be considered for admission."
            if 0 < student_mark < 66 else
            "You cannot obtain negative points."
            if student_mark < 0 else
            "You cannot obtain so many points."
        )
    except ValueError:
        return "Invalid input. Please enter a valid number."


if __name__ == '__main__':
    first_student = "85"
    second_student = "blablabla"
    third_student = "-1"
    fourth_student = "115"
    fifth_student = input("Enter a number of points: \n")
    print(pass_mark(first_student))
    print(pass_mark(second_student))
    print(pass_mark(third_student))
    print(pass_mark(fourth_student))
    print(pass_mark(fifth_student))
