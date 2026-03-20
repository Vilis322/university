import telebot
import random
from telebot import types

bot = telebot.TeleBot("TOKEN")

user_score = 0
bot_score = 0
limit_score = 10


@bot.message_handler(func=lambda message: message.text.capitalize() if user_score == limit_score else bot_score == limit_score)
def handle_play_again(message):
    global user_score
    global bot_score
    global limit_score

    if message.text == "Да":
        user_score = 0
        bot_score = 0
        start(message, True)
    elif message.text == "Нет":
        user_score = 0
        bot_score = 0
        bot.send_message(message.chat.id, "Спасибо за игру! До новых встреч!")  # exit()
    else:
        bot.reply_to(message, "Был введён некорректный ответ. Выберите ответ из 'Да' или 'Нет'.", reply_markup=markup_play_again())


@bot.message_handler(commands=["start"])
def start(m, res=False):
    if res:
        bot.send_message(m.chat.id, "Вы решили сыграть ещё раз. Играем до 10 очков.",
                         reply_markup=markup_pap_st_scis())
    else:
        bot.send_message(m.chat.id, "Привет, я бот, играющий в Камень-ножницы-бумага. Играем до 10 очков. Сыграем?",
                         reply_markup=markup_pap_st_scis())


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global user_score
    global bot_score
    global limit_score

    game_list = ["камень", "ножницы", "бумага"]
    user_choice = message.text.lower()

    if user_choice in game_list:
        bot_choice = random.choice(game_list)
        if user_choice == bot_choice:
            bot.reply_to(message, f"Ваш выбор {user_choice}, выбор бота {bot_choice}, результат данной партии - ничья.")
        elif (user_choice == "камень" and bot_choice == "ножницы") or \
                (user_choice == "ножницы" and bot_choice == "бумага") or \
                (user_choice == "бумага" and bot_choice == "камень"):
            user_score += 1
            bot.reply_to(message, f"Ваш выбор {user_choice}, выбор бота {bot_choice}, Вы победили.\nВаш счёт {user_score}, "
                                  f"счёт бота {bot_score}.")
        else:
            bot_score += 1
            bot.reply_to(message, f"Ваш выбор {user_choice}, выбор бота {bot_choice}, бот победил.\nВаш счёт {user_score}, "
                                  f"счёт бота {bot_score}.")
    else:
        bot.reply_to(message, "Был введён некорректный ответ. Пожалуйста, выбирайте между вариантами 'Камень',"
                              " 'Ножницы' или 'Бумага'", reply_markup=markup_pap_st_scis())

    if user_score == limit_score:
        bot.send_message(message.chat.id, "Вы победили! Поздравляю! Хотите сыграть ещё раз?",
                         reply_markup=markup_play_again())
    elif bot_score == limit_score:
        bot.send_message(message.chat.id, "Бот победил. Не расстраивайтесь! Хотите сыграть ещё раз?",
                         reply_markup=markup_play_again())


def markup_pap_st_scis():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stone_button = types.KeyboardButton("Камень")
    scissors_button = types.KeyboardButton("Ножницы")
    paper_button = types.KeyboardButton("Бумага")
    markup.add(stone_button, scissors_button, paper_button)
    return markup


def markup_play_again():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes_button = types.KeyboardButton("Да")
    no_button = types.KeyboardButton("Нет")
    markup.add(yes_button, no_button)
    return markup


bot.polling(none_stop=True, interval=0)
