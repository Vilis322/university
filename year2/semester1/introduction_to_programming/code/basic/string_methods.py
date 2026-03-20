# С помощью метода '.istitle' производится проверка на заглавные буквы в каждом слове из заданной строки. Например:
country = "United States of America"
islands = "United States Virgin Islands"
print(f"First result istitle: {country.istitle()}, second result istitle: {islands.istitle()}")

# Для проверки вхождения подстроки в строку можно использовать оператор 'in' или метод '.find'.

# С помощью оператора 'in':
message = "I will create a new legendary game!"
sub_message = "Legendary"
# Если необходимо провести поиск без учёта регистра, то можно использовать метод '.lower'
if sub_message.lower() in message.lower():
    print("Substring has founded.")

# С помощью метода '.find':
reply_message = "Go ahead."
if reply_message.find("ahead"):
    print("Substring has founded.")

# Найти индекс первого вхождения подстроки в строку можно с помощью методов '.find' и '.index':
account_number = input("Enter your account number, please: ")
print(account_number.find("2"))
# Также вторым аргументом можно записать индекс, с которого будет начинаться поиск подстроки (актуально и для '.find'):
print(account_number.index("2", 0))

# Подсчитать количество символов в строке можно с помощью функции '(len)':
index_number = "I have a question about your homework."
print(f"The number of symbols in string is {len(index_number)}")

# Подсчитать количество раз, которое встречается определённый символ в строке можно с помощью метода '.count':
symbol_o = "O, hello, how are you?"
print(symbol_o.lower().count("o"))

# Сделать первый символ заглавной буквой можно с помощью метода '.capitalize':
greeting = "hello, world"
print(greeting.capitalize())

# f-строки или интерполяция используются как инструмент для имплементации значений переменных и выражений внутрь строк:
first_int = 5
second_int = 5
result_sum_int = first_int + second_int
print(f"Результатом сложения {first_int} и {second_int} будет {result_sum_int}")
print(f"Результатом умножения {result_sum_int} на само себя будет {result_sum_int * result_sum_int}")

# Для поиска подстроки в заданной части строки можно воспользоваться методом '.find' и указанием диапазона поиска:
search_w = "I have to work"
print(search_w.find("w", 5, -1))  # где '5' - начальный индекс диапазона поиска, а '-1' - конечный

# Вместо '-1' как последний индекс строки можно указать 'len()'
search_l = "Hello, world!"
print(search_l.find("l", 1, len(search_l)))

# Чтобы узнать, что в строке содержатся только цифры, необходимо использовать метод '.isdigit':
password = input("Enter your password: ")
if password == "123456" and password.isdigit():
    print(f"Password is correct, {password.isdigit()}")
else:
    print("Password isn't correct")

# Также можно использовать метод '.isdecimal', чтобы узнать, что строка состоит только из десятичных цифр:
numbers = "123456"
print(numbers.isdecimal())

# Ещё есть метод '.isnumeric', определяющий, являются ли все символы в строке числовыми:
arabic_number = "123"
roman_number = "Ⅶ"  # может быть интерпретировано как римское число и результатом также будет True
print(arabic_number.isnumeric())
print(roman_number.isnumeric())

# Разделить строку с помощью заданного символа можно с помощью нескольких способов:
# первым является способ разделения с начала строчки по левой стороне метод '.partition':
separation_by_the_right_side = "You have to prepare for exam, Bill!"
print(separation_by_the_right_side.partition(','))

# вторым способом разделения является метод '.partition', разделяющий строку с конца по левой стороне:
separation_by_the_left_side = "I have already prepared, dad"
print(separation_by_the_left_side.rpartition(','))

# также строчку можно разделить с помощью метода '.split', имеющий параметр количества разделений по разделителю:
separation = "Juice, milk, meat, bread and butter"
print(separation.split(',', 2))  # с методом '.split' разделение начинается с начала строчки с левой стороны

# последний способ разделения выполняется методом '.rsplit', также имеющим параметр количества разделений:
print(separation.rsplit(',', 2))  # метод '.rsplit' начинает разделение с конца строчки с правой стороны

# для проверки строки на использование только символов нижнего регистра используется метод '.islower':
low_symbols = "hi, how are you?"  # результатом будет булево значение True, ведь все символы в строке строчные
low_symbols_2 = "Hi, how are you?"  # результатом будет булево значение False, так как есть заглавный символ
if low_symbols.islower():
    print(f"Все символы в данной строке являются строчными\nРезультатом проверки будет {low_symbols.islower()}")
if not low_symbols_2.islower():
    print(f"Не все символы в данной строке являются строчными\nРезультатом проверки будет {low_symbols_2.islower()}")

# чтобы проверить, начинается ли строка со строчной буквы, можно также использовать метод '.islower', указав индекс:
if low_symbols[0].islower():
    print(f"Первый символ строки является строчным\nРезультатом проверки будет {low_symbols[0].islower()}")
# помимо индекса первого символа можно указать любой другой диапазон поиска индексов строчных символов в строке:
if low_symbols_2[1::]:
    print(f"""Все символы в строке, кроме первого, являются строчными
Результат проверки будет {low_symbols_2[1::].islower()}""")

# для того чтобы "перевернуть" строку, можно использовать срез строки:
reverse_string = "Эту строку необходимо перевернуть в обратную сторону"
print(reverse_string[::-1])

# для объединения списка строк в одну строку, разделённую дефисами, необходимо использовать метод '.join':
shopping_list = ["milk", "apple", "meat"]
to_do_list = ["reading", "singing"]
print("-".join(shopping_list) + "-" + "-".join(to_do_list))

# для того, чтоб узнать, являются ли все символы в строке только алфавитными, надо использовать метод '.isalpha':
alphabetic_symbols = input("Введите текст, составленный исключительно из алфавитных символов: ")
if alphabetic_symbols.isalpha():
    print(f"Ваш текст: {alphabetic_symbols}\nТекст состоит только из алфавитных символов.")
else:
    print(f"Ваш текст: {alphabetic_symbols}\nТекст состоит не только из алфавитных символов.")

# для замены всех вхождений подстроки в заданной строке можно использовать метод '.replace':
replace_string = "Сегодня 25 апреля"
print(replace_string.replace("25", "26"))

# для проверки строки на содержание в ней только алфавитно-цифровых символов используется метод '.isalnum':
first_symbols_list = "123hey"
second_symbols_list = "123 hey"
third_symbols_list = "123/hey"

if first_symbols_list.isalnum():
    print("Все символы в строке являются алфавитно-цифровыми.")
else:
    print("Не все символы в строке являются алфавитно-цифровыми.")

if second_symbols_list.isalnum():
    print("Все символы в строке являются алфавитно-цифровыми.")
else:
    print("Не все символы в строке являются алфавитно-цифровыми.")

if third_symbols_list.isalnum():
    print("Все символы в строке являются алфавитно-цифровыми.")
else:
    print("Не все символы в строке являются алфавитно-цифровыми.")

# для проверки начала строки на наличие последовательности определённых символов используется метод '.startswith':
print(first_symbols_list.startswith("123"))
# для проверки конца строки на наличие последовательности определённых символов используется метод '.endswith':
print(first_symbols_list.endswith("123"))

# для проверки на использование в строке только символов пробела используется метод '.isspace':
only_space = "   "
print("Результатом проверки строки на наличие только символов пробела будет " + str(only_space.isspace()))

# для приведения всех символов в строке к верхнему регистру используется метод '.title':
title_symbols = "каждый первый символ в строке должен быть заглавным"
print(title_symbols.title())

# замена подстроки 2 на подстроку two
string = "2 years old"
print(string.replace("2", "two"))

# первый вариант второго задания
string = "123+(d+(a+b)+12)=22"
print(f"{string.replace('(', '*(', 1).replace(')', ')*', -1)}")

# второй вариант второго задания
string = input("Введите строку, используя символы открывающей и закрывающей скобок: ")

if string.find("(") != -1 and string.rfind(")") != -1:
    print(string[:string.find("(")] + "*" + string[string.find("("):string.rfind(")") + 1] + "*"
          + string[string.rfind(")") + 1:])
else:
    print("Ошибка: в строке отсутствует скобка!")

# третий вариант второго задания
string = input("Введите строку, используя символы открывающей и закрывающей скобок: ")
print(string.replace('(', '*(', 1).replace(')', ')*', -1))

string = input("Введите пароль: ")
if string.startswith("Password"):
    print("Пароль введён верно.")
else:
    print("Пароль введён неправильно.")
