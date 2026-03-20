def user_input():

    word = input("Please enter a word:\n")
    return word


def is_palindrome(word):
    word_for_check = word.lower().strip()
    return word_for_check == word_for_check[::-1]


def main():
    word = user_input()
    print("Your word is palindrome!") if is_palindrome(word) else print("Your word is not a palindrome!")


if __name__ == "__main__":
    main()
