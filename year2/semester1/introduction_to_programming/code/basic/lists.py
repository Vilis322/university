# Первое задание
number_list = [int(x) for x in input("Введите список целых чисел через пробел: ").split()]
print(f"Сумма введённых Вами чисел равна {sum(number_list)}")

# Второе задание
eating_list = input("Введите список ваших любимых блюд: ").split()
print(f"Далее указано каждое второе блюдо из списка: {eating_list[1::2]}")

# Третье задание
number_list = [int(x) for x in input("Введите список из не менее чем пяти целых чисел через пробел: ").split()]
average_sum = sum(number_list) / len(number_list)
print(f"Среднее арифметическое введённых чисел равно: {float(average_sum):.3f}")

# Четвёртое задание
string = input("""Введите символы О и Р, обозначающий орёл и решка соответственно, в строке без пробелов для 
дальнейшего подсчёта процента выпадения обоих сторон монеты: """)
number_of_heads = string.lower().count("о")
number_of_tails = string.lower().count("р")
print(f"Процент выпадения орла, исходя из введённых Вами данных, равен {(number_of_heads / len(string)) * 100}")
print(f"Процент выпадения решки, исходя из введённых Вами данных, равен {(number_of_tails / len(string)) * 100}")
