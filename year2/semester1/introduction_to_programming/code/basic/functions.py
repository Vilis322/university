# Первое задание:
def calculate_average(number_list):
    while True:
        try:
            number_list = [int(num) for num in number_list]
            total = sum(number_list)
            average = total / len(number_list)
            return average
        except ValueError:
            print("Ошибка ввода! Были введены некорректные числа.")
            while True:
                retry = input("Хотите повторить ввод чисел для поиска среднего значения? (да/нет): ")
                if retry.lower() == 'нет':
                    print("Вы решили завершить программу.")
                    return None
                elif retry.lower() == 'да':
                    number_list = input("Введите числа через пробел для поиска среднего значения: ").split()
                    break
                else:
                    print("Был введён некорректный ответ. Пожалуйста, введите ответ 'да' или 'нет' для продолжения.")


numbers = input("Введите числа через пробел для поиска среднего значения: ").split()
print(f"Среднее значение: {calculate_average(numbers)}.")


# Второе задание:
def is_even(boolean):
    while True:
        try:
            boolean = int(boolean)
            return boolean % 2 == 0
        except ValueError:
            print("Было введено некорректное число.")
            while True:
                retry = input("Если вы хотите заново ввести число, то введите 'да'. Иначе введите 'нет': ")
                if retry.lower() == 'да':
                    boolean = int(input("Введите число для дальнейшей проверки его на чётность: "))
                    break
                elif retry.lower() == 'нет':
                    print("Вы решили завершить программу.")
                    return None
                else:
                    print("Был введён некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")


multiplicity = input("Введите число для дальнейшей проверки его на чётность: ")
result = is_even(multiplicity)

output_messages = {True: "чётным", False: "нечётным"}

if result is not None:
    print(f"Число введённое Вами является {output_messages[result]}.")

print(result)


# Третье задание:
def count_vowels(vowels):
    vowels = vowels.lower()
    count = sum(vowels.count(vowel) for vowel in "аэоиыуяеюё")
    return count


string = input("Введите слово для подсчета гласных букв во введенном слове: ")
print(f"Количество гласных букв во введенном Вами слове равно: {count_vowels(string)}.")


# Четвёртое задание:
def find_max(numbers):
    while True:
        try:
            numbers = [int(number) for number in numbers.split()]
            max_number = numbers[0]
            for number in numbers[1:]:
                if number > max_number:
                    max_number = number
            return max_number
        except ValueError:
            print("Было введено некорректное число или числа.")
            while True:
                retry = input("Если Вы хотите заново ввести список чисел, то введите 'да'. Иначе введите 'нет': ")
                if retry.lower() == 'да':
                    numbers = input("Введите список, состоящий из чисел, разделённых знаком пробела: ")
                    break
                elif retry.lower() == 'нет':
                    print("Вы решили завершить программу.")
                    return None
                else:
                    print("Был введён некорректный ответ. Пожалуйста, для продолжения введите 'да' или 'нет'.")


user_numbers = input("Введите список, состоящий из чисел, разделённых знаком пробела: ")
result = find_max(user_numbers)

if result is not None:
    print(f"Максимальное число из введённых Вами равно {result}.")


# Пятое задание:
def reverse_string(string):
    return string[::-1]


user_string = input("Введите строку для последующего вывода введённой строки в обратном порядке: ")
print(f"Введённая строка в обратном порядке: {reverse_string(user_string)}.")


# Шестое задание:
def is_palindrome(string):
    return string == string[::-1]


user_string = input("Введите строку: ")
if is_palindrome(user_string):
    print("Строка читается одинаково в обе стороны.")
else:
    print("Строка не читается одинаково в обе стороны.")
print(is_palindrome(user_string))


# Седьмое задание:
def factorial(n):
    while True:
        try:
            n = int(n)
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        except ValueError:
            print("Было введено некорректное число.")
            while True:
                retry = input("Если вы хотите заново ввести факториал числа, то введите 'да'. Иначе введите 'нет': ")
                if retry.lower() == 'да':
                    n = input("Введите число для последующего возврата факториала введённого числа: ")
                    break
                elif retry.lower() == 'нет':
                    print("Вы решили завершить программу.")
                    return None
                else:
                    print("Был введён некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")


user_n = input("Введите число для последующего возврата факториала введённого числа: ")
result = factorial(user_n)

if result is not None:
    print(f"Факториал введённого Вами числа является число {result}.")


# Восьмое задание:
def is_prime(n):
    while True:
        try:
            n = int(n)
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        except ValueError:
            print("Было введено некорректное число.")
            while True:
                retry = input("Если вы хотите заново ввести число на проверку, то введите 'да'. Иначе введите 'нет': ")
                if retry.lower() == 'да':
                    n = input("Введите число для последующей проверки, простое ли введённое число: ")
                    break
                elif retry.lower() == 'нет':
                    print("Вы решили завершить программу.")
                    return None
                else:
                    print("Был введён некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")


user_n = input("Введите число для проверки, является ли введённое число простым: ")
relevance_dictionary = {True: 'является простым числом.', False: 'не является простым числом.'}

result = is_prime(user_n)

if result is not None:
    print(f"Введённое Вами число {relevance_dictionary[result]}")
print(result)


# Девятое задание:
def generate_fibonacci(n):
    while True:
        try:
            fibonacci_sequence = []
            n = int(n)
            a, b = 0, 1
            for i in range(n):
                fibonacci_sequence.append(str(a))
                a, b = b, a + b
            return ', '.join(fibonacci_sequence)
        except ValueError:
            print("Было введено некорректное число.")
            while True:
                retry = input("Если вы хотите заново ввести число на проверку, то введите 'да'. Иначе введите 'нет': ")
                if retry.lower() == 'да':
                    n = input("Введите число для последующей проверки, простое ли введённое число: ")
                    break
                elif retry.lower() == 'нет':
                    print("Вы решили завершить программу.")
                    return None
                else:
                    print("Был введён некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")


user_n = input("Введите число, обозначающее количество чисел Фибоначчи, для последующего вывода: ")

result = generate_fibonacci(user_n)

if result is not None:
    print(f"Первые числа Фибоначчи из введённых Вами: {result}.")


# Десятое задание:
def capitalize_names():
    names = input("Введите имена, разделенные пробелами: ").split()
    capitalized_names = []
    for name in names:
        capitalized_names.append(name.capitalize())
    return ', '.join(capitalized_names)


print(f"Введённые Вами имя с приведённым первым символом к верхнему регистру: {capitalize_names()}.")
