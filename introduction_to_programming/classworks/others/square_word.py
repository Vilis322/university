def user_input():
    word = input("Enter any word:\n")
    return word


def main():
    word = user_input()
    square_word = len(word)

    for i in range(square_word):
        print(word.upper())


if __name__ == "__main__":
    main()