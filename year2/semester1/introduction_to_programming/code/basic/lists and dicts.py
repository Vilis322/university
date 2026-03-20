import sys

account1 = {"login": "ivan", "password": "q1"}
account2 = {"login": "petr", "password": "q2"}
account3 = {"login": "olga", "password": "q3"}
account4 = {"login": "anna", "password": "q4"}

user1 = {"name": "Иван", "age": 20, "account": account1}
user2 = {"name": "Петр", "age": 18, "account": account2}
user3 = {"name": "Ольга", "age": 25, "account": account3}
user4 = {"name": "Анна", "age": 27, "account": account4}

user_list = [user1, user2, user3, user4]

tries = 3
try_messages = {3: "У вас осталось 3 попытки.", 2: "У вас осталось 2 попытки.", 1: "У вас осталась 1 попытка."}
key_message = input(f"Введите ключ ('name' или 'login') без кавычек для получения информации. {try_messages[tries]} "
                    f"\nИли введите 'выход' без кавычек для прерывания программы: ").lower().strip()
while tries > 0:
    if key_message == 'login':
        print(f"""Был введён корректный ключ.
Значение ключа 'account' для пользователя 1: {account1['login']};
значение ключа 'account' для пользователя 2: {account2['login']};
значение ключа 'account' для пользователя 3: {account3['login']};
значение ключа 'account' для пользователя 4: {account4['login']}.""")
        break
    elif key_message == 'name':
        print(f"""Был введён корректный ключ.
Значение ключа 'name' для пользователя 1: {user1['name']};
значение ключа 'name' для пользователя 2: {user2['name']};
значение ключа 'name' для пользователя 3: {user3['name']};
значение ключа 'name' для пользователя 4: {user4['name']}.""")
        break
    elif key_message == 'выход':
        sys.exit("Программа завершена по желанию пользователя.")
    else:
        tries -= 1
        if tries == 0:
            sys.exit("Вы исчерпали свои попытки для корректного ввода ключа.\nПожалуйста, попробуйте позже.")
        key_message = input(f"Был введён некорректный ключ. {try_messages[tries]}\n"
                            f"Пожалуйста, введите корректный ключ 'name' или 'login' без кавычек.\n"
                            "Или введите 'выход' без кавычек для завершения программы: ").lower().strip()

tries_index = 3
index = input(f"Для получения информации о пользователе необходимо ввести его порядковый номер.\n"
              f"У вас осталось {try_messages[tries_index]}\nВведите порядковый номер пользователя: ").strip()
while tries_index != 0:
    if index.isdigit() and 0 < int(index) <= len(user_list):
        index = int(index)
        user = user_list[index-1]
        account = user['account']
        print(f"""Вы выбрали пользователя под номером {index}. Вот информация по данному пользователю:
Имя: {user['name']};
возраст: {user['age']};
логин: {account['login']};
пароль: {account['password']}.""")
        break
    else:
        tries_index -= 1
        if tries_index == 0:
            sys.exit("Вы исчерпали попытки корректного ввода номера.\nПожалуйста, попробуйте позже.")
        index = input(f"""Был введён некорректный порядковый номер. {try_messages[tries_index]}
Пожалуйста, введите корректный порядковый номер для получения информации о пользователе: """).strip()

tries_to_move = 3
index_to_move = input(f"Для переноса выбранного пользователя в конец списка необходимо ввести его порядковый номер.\n"
                      f"{try_messages[tries_to_move]} Введите порядковый номер пользователя: ").strip()
while tries_to_move != 0:
    if index_to_move.isdigit() and 0 < int(index_to_move) <= len(user_list):
        index_to_move = int(index_to_move)
        copy_user_list = user_list.copy()
        user_to_move = user_list[index_to_move-1]
        user_list.remove(user_to_move)
        user_list.append(user_to_move)
        print(f"Пользователь {user_to_move['name']} был перемещён в конец списка.\nСписок до изменения: "
              f"{copy_user_list}.\nСписок после изменения: {user_list}.")
        break
    else:
        tries_to_move -= 1
        if tries_to_move == 0:
            sys.exit("Вы исчерпали попытки корректного ввода номера.\nПожалуйста, попробуйте позже.")
        index_to_move = input(f"Был введён некорректный порядковый номер.\n{try_messages[tries_to_move]}\nПожалуйста,"
                              f" введите корректный порядковый номер: ").strip()

ages = [age['age'] for age in user_list]
average_age = sum(ages) / len(ages)
print(f"Средний возраст пользователей из списка составляет {average_age} лет.")
