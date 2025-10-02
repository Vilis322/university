# Первое задание:
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
print(primes[0:5 + 1])

# Второе задание:
data = 'Python для продвинутых!'
print(tuple(data))

# Третье задание:
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))

# Четвёртое задание:
first_string = set(input("Введите строку, состоящую из разных неповторяющихся цифр: "))
second_string = set(input("Введите строку, состоящую из разных неповторяющихся цифр: "))
if first_string == second_string:
    print("Для записи этих строк были использованы одинаковые наборы цифр.")
else:
    print("Для записи этих строк были использованы разные наборы цифр.")

# Пятое задание, первый вариант:
string = input("Введите список, состоящий из разных слов (неважно через запятую или нет): ")
print(len(set(string.lower().replace(",", "").replace(".", "").split())))

# Пятое задание, второй вариант:
string = input("Введите список, состоящий из разных слов (неважно через запятую или нет): ")
point_and_coma = ",."
translation = "  "
print(len(set(string.lower().translate(string.maketrans(point_and_coma, translation)).split())))

# Шестое задание:
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) 
when I was three, and, save for a pocket of warmth in the darkest past, nothing of her 
subsists within the hollows and dells of memory, over which, if you can still stand my style 
(I am writing under observation), the sun of my infancy had set: surely, you all know those redolent 
remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and 
traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
punctuation_marks = ";:,.()"
translation = "      "
sentence = sentence.lower().translate(str.maketrans(punctuation_marks, translation))
print(' '.join(sorted(set(sentence.split()))))

# Седьмое задание
string = input("Введите натуральные числа от 0 до 9 в любом порядке (неважно с пробелом или без: ")
numbers_translation = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7":
                       "seven", "8": "eight", "9": "nine"}
translated_string = " ".join([numbers_translation.get(num, num) for num in string])
print(translated_string)
