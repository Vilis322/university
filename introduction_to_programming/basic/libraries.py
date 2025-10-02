# Первое задание:
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


password_length = int(input("Введите желаемое количество символов в пароле: "))
password = generate_password(password_length)
print(password)

# Второе задание:
from datetime import datetime


def calculate_age(birth_date):
    current_date = datetime.now()
    age = current_date.year - birth_date.year

    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


birth_date_str = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")

age = calculate_age(birth_date)

age_dict = {(1, 21, 31, 41, 51, 61, 71, 81, 91): "год",
            (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
                "года"}

key = next((key for key in age_dict.keys() if isinstance(key, tuple) and age in key), None)

if key is not None:
    print(f"Ваш возраст составляет {age} {age_dict[key]}.")
else:
    print(f"Ваш возраст составляет {age} лет.")

# Третье задание:
import collections


def count_words(filename):
    word_counts = collections.Counter()

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            word_counts.update(words)

    return word_counts


filename = "your_file.txt"  # Укажите путь к необходимому файлу
word_counts = count_words(filename)

for word, count in word_counts.items():
    print(f"Слово {word} употребилось {count} раз.")

