def user_input():
    try:
        id_number = input("Please enter your Estonian Personal Identification Number:\n")

        if not id_number.isdigit():
            raise ValueError("Estonian Personal Identification Number must be only numerical!")

        if not len(id_number) == 10:
            raise ValueError("Estonian Personal Identification Number have to be as 10 numbers!")

        return id_number
    except ValueError as e:
        print(e)


def main():
    id_number = user_input()
    print("You are a female!") if int(id_number[0]) % 2 == 0 else print("You are a male!")


if __name__ == "__main__":
    main()
