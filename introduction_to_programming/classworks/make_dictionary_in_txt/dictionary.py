from pathlib import Path
from time import sleep


def read_dictionary_in_file(file):
    dictionary = {}
    try:
        file_path = Path(file).read_text(encoding='utf8').splitlines()
        for line in file_path:
            words = line.strip().split("\t")
            if len(words) == 2:
                key, value = words
                dictionary[key] = value
    except FileNotFoundError as e:
        print('File does not exists!')
        print(str(e))

    return dictionary


def append_to_file(file, word, translation):
    file_path = Path(file)
    with file_path.open("a", encoding="utf-8") as f:
        f.write(f"{word}\t{translation}\n")


def main():
    dictionary = read_dictionary_in_file("dictionary.txt")

    while True:
        word = input("Enter a word or done, if you want to finish work with dictionary: ").strip().lower()

        if word == "done":
            break

        if word in dictionary:
            print(f"This word already in dictionary, here is translation: {dictionary[word]}")
        else:
            translation = input("This word does not in dictionary, enter a translation: ").strip().lower()
            dictionary[word] = translation
            append_to_file("dictionary.txt", word, translation)

    for key, value in dictionary.items():
        print(f"For word '{key}' translation is '{value}'")
        sleep(1)


if __name__ == "__main__":
    main()
