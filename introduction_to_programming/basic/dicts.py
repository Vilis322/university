# Создание словаря в фигурных скобках:
# my_dict = {"apple": 1, "banana": 2, "orange": 3}

# Создание словаря с помощью функции dict():
# my_dict2 = dict(apple=1, banana=2, orange=3)

# Доступ к элементам словаря осуществляется по ключу с помощью оператора []:
# my_dict = {"apple": 1, "banana": 2, "orange": 3}
# print(my_dict["apple"])

# Добавление нового элемента в словарь:
# my_dict = {"apple": 1, "banana": 2, "orange": 3}
# my_dict["grape"] = 4
# print(my_dict)

# Изменение значения элемента по ключу:
# my_dict = {"apple": 1, "banana": 2, "orange": 3}
# my_dict["orange"] = 4
# print(my_dict)

# Удаление элемента из словаря:
# my_dict = {"apple": 1, "banana": 2, "orange": 3}
# del my_dict["banana"]
# print(my_dict)

# Проверка наличия ключа в словаре:
# my_dict = {"apple": 1, "banana": 2, "orange": 3}
# print("apple" in my_dict)

# clear() - удаляет все элементы из словаря:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# my_dict.clear()
# print(my_dict)

# copy() - создает копию словаря:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# new_dict = my_dict.copy()
# print(new_dict)

# get(key, default=None) - возвращает значение ключа key, если он есть в словаре, иначе возвращает значение
# по умолчанию default:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# print(my_dict.get("apple"))
# print(my_dict.get("pear", 0))

# items() - возвращает список кортежей, содержащих все пары ключ-значение в словаре:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# print(my_dict.items())

# keys() - возвращает список всех ключей в словаре:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# print(my_dict.keys())

# values() - возвращает список всех значений в словаре:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# print(my_dict.values())

# pop(key, default=None) - удаляет элемент из словаря по ключу key и возвращает его значение, если ключ найден.
# Если ключ не найден, возвращает значение по умолчанию default, если оно указано:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# print(my_dict.pop("apple"))
# print(my_dict.pop("pear", 0))
# print(my_dict)

# popitem() - удаляет и возвращает последнюю пару ключ-значение из словаря в виде кортежа:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# print(my_dict.popitem())
# print(my_dict)

# update(dict2) - обновляет словарь парами ключ-значение из другого словаря dict2:
# my_dict = {"apple": 2, "banana": 3, "orange": 4}
# new_dict = {"pear": 5, "kiwi": 6}
# my_dict.update(new_dict)
# print(my_dict)

# Первое задание:
my_information = dict(name="Кирилл", age="24", favorite_color="зелёный")
print(f"Меня зовут {my_information['name']}, мне {my_information['age']}, мой любимый цвет "
      f"{my_information['favorite_color']}.")

# Второе задание:
films_dict = {"Славные парни": ["Мартин Скорсезе", "Ирвин Уинклер", "Николас Пиледжи, Мартин Скорсезе",
                                "Роберт Де Ниро", "Рэй Лиотта", "Джо Пеши", "Лоррейн Бракко", "Пол Сорвино"],
              "Выстрел в пустоту": ["Рик Роман Во", "Джонатан Кинг, Мишель Литвак, Гари Майкл Уолтерс", "Рик Роман Во",
                                    "Николай Костер-Вальдау", "Джон Бернтал", "Лэйк Белл", "Джеффри Донован",
                                    "Эмори Коэн"],
              "Джентльмены": ["Гай Ричи", "Гай Ричи", "Гай Ричи, Айван Эткинсон, Марн Дэвис", "Чарли Ханнэм",
                              "Генри Голдинг", "Мишель Докери", "Колин Фаррел", "Хью Грант", "Мэтью Макконахи",
                              "Джереми Стронг", "Эдди Марсан"],
              "Джон Уик": ["Чад Стахелски, Дэвид Литч", "Бэзил Иваник, Дэвид Литч, Ева Лонгория, Майк Уитерилл",
                           "Дерек Колстад", "Киану Ривз", "Михаэль Нюквист", "Альфи Аллен", "Эдрианн Палики",
                           "Бриджит Мойнахан", "Дин Уинтерс", "Иэн Макшейн", "Джон Легуизамо", "Уиллем Дефо"]}
film_name = input("Введите название известного остросюжетного криминального триллера для получения информации: ")
films_dict = {film.lower(): films_dict[film] for film in films_dict}
film_name = film_name.lower()
if film_name in films_dict:
    print(f"""Вот список продюсеров, режиссёров, авторов сценария и актёров введённого фильма:
    Режиссёр(ы): {films_dict[film_name][0]}
    Продюсер(ы): {films_dict[film_name][1]}
    Автор(ы) сценария: {films_dict[film_name][2]}
    В главных ролях: {', '.join(films_dict[film_name][3::])}""")
else:
    print("К сожалению, данного фильма в списке нет.")

# Третье задание:
country_dict = {"name": "Эстония", "capital": "Таллинн", "population": "1 331 000"}
print(f"""Столицей страны {country_dict["name"]} является город {country_dict["capital"]};
Численность населения составляет {country_dict["population"]} человек.""")

# Четвёртое задание:
videogames_dict = {"Elden Ring": ["From Software", "Bandai Namco", "25 февраля 2022 года", "Action/RPG"],
                   "Bloodborne": ["From Software", " Sony Interactive Entertainment", "24 марта 2015 года",
                                  "Action/RPG, horror"],
                   "Red Dead Redemption 2": ["Rockstar Games", "Rockstar Games", "26 октября 2018 года",
                                             "Western, Third person shooter"],
                   "Mass Effect": ["BioWare", "Electronic Arts", "16 ноября 2007 года", "Action/RPG, space opera"],
                   "Death Stranding": ["Kojima Productions, Guerilla Games", " Sony Interactive Entertainment",
                                       "8 ноября 2019 года", "Adventure, Third person shooter"]}
user_string = input("Введите название Вашей любимой игры для получения информации про неё: ")
user_string = user_string.lower()
videogames_dict = {game.lower(): videogames_dict[game] for game in videogames_dict}
if user_string in videogames_dict:
    print(f"""Вот информация по данной игре: 
    Разработчики: {videogames_dict[user_string][0]}
    Издатель: {videogames_dict[user_string][1]}
    Дата выхода: {videogames_dict[user_string][2]}
    Жанр: {videogames_dict[user_string][3]}""")
else:
    print("К сожалению, данная видеоигра отсутствует в списке.")

# Пятое задание:
baltic_dict = {"Эстония", "Латвия", "Литва"}
scandinavian_dict = {"Швеция", "Финляндия", "Норвегия", "Дания", "Исландия"}
capital_dict = {"Эстония": "Таллин", "Латвия": "Рига", "Литва": "Вильнюс", "Швеция": "Стокгольм", "Финляндия":
                "Хельсинки", "Норвегия": "Осло", "Дания": "Копенгаген", "Исландия": "Рейкьявик"}
country_name = input("Введите название одной страны, входящей в состав Прибалтики или Скандинавского полуострова: ")
country_name = country_name.title()
if country_name in capital_dict:
    if country_name in baltic_dict:
        print(f"Столицей данной страны является город {capital_dict[country_name]}")
        print("Введённая вами страна является частью Прибалтийского региона.")
    elif country_name in scandinavian_dict:
        print(f"Столицей данной страны является город {capital_dict[country_name]}")
        print("Введённая вами страна является частью Скандинавского полуострова.")
else:
    print("Введённая вами страна не является частью Прибалтийского региона или Скандинавского полуострова.")

# Шестое задание:
price_for_fruits_dict = {"яблоки": 4.0, "апельсины": 8.4, "бананы": 3.6, "мандарины": 4.5, "груши": 3.8, "грейпфрут":
                         7.4, "вишня": 2.2, "голубика": 10.5, "черешня": 6.0, "абрикос": 4.2}
fruit_plural_dict = {"яблоки": "яблок", "апельсины": "апельсинов", "бананы": "бананов", "мандарины": "мандаринов",
                     "груши": "груш", "грейпфрут": "грейпфрутов", "вишня": "вишен", "голубика": "голубики", "черешня":
                         "черешни", "абрикос": "абрикосов"}
print("Добро пожаловать во фруктовую лавку!")
while True:
    fruit_name = input("Введите название фруктов, которые вы желаете купить: ")
    fruit_name = fruit_name.lower()
    if fruit_name not in price_for_fruits_dict:
        print("К сожалению, данные фрукты отсутствуют в нашей лавке.")
        answer_customer = input("Если Вы желаете купить ещё какие-то фрукты, то напишите 'да': ")
        if answer_customer.lower() == "да":
            continue
        else:
            print("В таком случае до свидания, хорошего дня!")
            break
    elif fruit_name in price_for_fruits_dict:
        fruit_weight = int(input("Введите желаемый вес выбранных вами фруктов в граммах: "))
        price_per_gram_dict = {fruit: price_for_fruits_dict[fruit] / 1000 for fruit in price_for_fruits_dict}
        total_price = fruit_weight * price_per_gram_dict[fruit_name]
        total_price = '{:.2f}'.format(total_price)
        print(f"Цена за {fruit_weight} грамм {fruit_plural_dict[fruit_name]} составляет {total_price} евро.")
        answer_customer = input("Если Вы желаете купить ещё какие-то фрукты, то напишите 'да': ")
        if answer_customer.lower() == "да":
            continue
        else:
            print("В таком случае до свидания, хорошего дня! Приходите снова!")
            break
