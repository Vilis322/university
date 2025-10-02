import telebot
from telebot import types
import os
import glob
import random


bot = telebot.TeleBot("TOKEN")

image_folder_path = 'mems'
image_files = glob.glob(os.path.join(image_folder_path, '*jpg'))


@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Привет! Я бот, поднимающий настроение! Если хочешь, чтобы я отправил тебе мем, то "
                                "нажми на кнопку!", reply_markup=markup_mem())


@bot.message_handler(content_types=["text"])
def mem_generator(message):
    if message.text == "Скинь мем":
        if image_files:
            random_image = random.choice(image_files)
            with open(random_image, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                image_files.remove(random_image)
        else:
            bot.reply_to(message, "Прости, но пока что у меня нет новых мемов(")
    else:
        bot.reply_to(message, "Я знаю только фразу 'Скинь мем'. Давай попробуем ещё раз!", reply_markup=markup_mem())


def markup_mem():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mem_button = types.KeyboardButton("Скинь мем")
    markup.add(mem_button)
    return markup


bot.polling(none_stop=True, interval=0)
