# Первое задание:

squared_list = [num**2 for num in range(1, 11)]
print(squared_list)

# Второе задание:

even_list = [num for num in range(1, 21) if num % 2 == 0]
print(even_list)

# Третье задание:

second_squared_list = [num**2 for num in range(1, 11) if num > 5]
print(second_squared_list)

# Четвёртое задание:
word = "Hello"
capital_list = [char.capitalize() for char in word]
print(capital_list)

# Пятое задание:
words = ['apple', 'banana', 'cherry', 'orange']
just_list = [fruit for fruit in words if len(fruit) > 5]
print(just_list)
