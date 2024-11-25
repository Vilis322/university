import re
from itertools import permutations
from pathlib import Path
import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_text_from_file(file):
    file_path = Path(file)
    try:
        with file_path.open('r', encoding='utf-8') as text:
            return text.read()
    except FileNotFoundError as e:
        print("File not found. Please check the parent directory and try again.")
        logging.error(f"File not found: {e}")
        return False


def main():
    war_and_peace = get_text_from_file('war_and_peace.txt')
    war_permutations = [''.join(i) for i in permutations('war')]
    if not war_and_peace:
        print("Something went wrong. Please check the file and try again.")
        return

    words_starting_with_p = re.findall(r'\bP\w*\b', war_and_peace)
    words_containing_war = re.findall(r'\b\w*(' + '|'.join(war_permutations) + r')\w*\b', war_and_peace)
    words_without_excluded_letters = re.findall(r'\b[^eiokl\s]*\b', war_and_peace)

    all_words = set(words_starting_with_p + words_containing_war + words_without_excluded_letters)
    print("Words starting with capital P or containing 'war' permutations or without e,i,o,k,l:")
    for word in all_words:
        print(word)


if __name__ == '__main__':
    main()
