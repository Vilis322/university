# Примеры исключений:
# 1. Обработка конкретного исключения:

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
    print("Результат деления:", result)
except ZeroDivisionError:
    print("Деление на ноль не допускается!")
except ValueError:
    print("Ошибка ввода числа!")

# 2. Обработка нескольких исключений одновременно:

try:
    num = int(input("Введите число: "))
    result = 10 / num
    print("Результат:", result)
except (ZeroDivisionError, ValueError):
    print("Ошибка ввода числа или деление на ноль!")

# 3. Использование общего исключения для перехвата всех ошибок:

try:
    num = int(input("Введите число: "))
    result = 10 / num
except Exception as e:
    print("Произошла ошибка:", str(e))

# Первое задание:

print("Данная программа принимает на ввод пользователя два отдельных значения.\nЕсли оба значения являются числами, то "
      "произойдёт суммирование введённых значений с последующим выводом.\nВ случае, если хотя бы одно вводимое значение"
      " не будет являться числовым, то произойдёт соединение двух строк с последующим выводом.")

first_value = input("Введите первое значение: ")
second_value = input("Введите второе значение: ")

try:
    first_number = int(first_value)
    second_number = int(second_value)
    result = first_number + second_number
    print("Оба введённых значения являются числовыми.\nНиже представлен результат суммирования введённых значений: ")
    print(result)
except ValueError:
    concatenation_result = "".join([first_value, second_value])
    print("Одно из введённых значений не является числовым.\nНиже представлен результат соединения двух значений: ")
    print(concatenation_result)

# Второе задание:


def check_password():
    try:
        password = input("Введите пароль: ")
        if not password:
            raise ValueError("Вы ввели пустой пароль.")
        if password.isdigit():
            raise ValueError("Ваш пароль состоит только из цифр.")
        print("Требования к паролю соблюдены.")
    except ValueError as e:
        print(e)


check_password()
