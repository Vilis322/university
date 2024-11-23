from time import sleep


def make_dictionary():
    dictionary = {}

    while True:
        word = input("Enter a word or done, if you want to finish work with dictionary: ").strip().lower()

        if word == "done":
            break

        if not word:
            print("The word cannot be empty. Please try again.")
            continue

        if word in dictionary:
            print(f"This word already in dictionary, here is translation: {dictionary[word]}")
        else:
            translation = input("This word does not in dictionary, enter a translation: ").strip().lower()
            dictionary[word] = translation

    for key, value in dictionary.items():
        print(f"For word '{key}' translation is '{value}'")
        sleep(1)


make_dictionary()
