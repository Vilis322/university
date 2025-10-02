import telebot
from telebot import types
import wikipedia
wikipedia.set_lang("ru")


class BotStateMachine:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.current_state = {}

        @self.bot.message_handler(commands=["start"])
        def handle_start(message):
            self.current_state[message.chat.id] = "start"
            self.bot.send_message(message.chat.id, "Привет! Я бот, заменяющий википедию. Введи свой запрос и по твоему "
                                                   "запросу на выбор я дам тебе несколько статей для изучения.")

        @self.bot.message_handler(content_types=["text"])
        def handle_text(message):
            chat_id = message.chat.id

            if chat_id in self.current_state and self.current_state[chat_id] == "start":
                self.current_state[chat_id] = "choose_article"
                results = wikipedia.search(message.text, results=3)
                self.titles_markup(chat_id, results)

            elif chat_id in self.current_state and self.current_state[chat_id] == "choose_article":
                self.current_state[chat_id] = "start"
                self.handle_article_choice(message)

        self.bot.polling(non_stop=True, interval=0)

    def titles_markup(self, chat_id, results):
        if results:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for result in results:
                markup.add(types.KeyboardButton(result))
            self.bot.send_message(chat_id, "Вот несколько статей, которые я нашёл по Вашему запросу, выберите "
                                           "интересующую Вас статью.", reply_markup=markup)
        else:
            self.bot.send_message(chat_id, "По Вашему запросу не было найдено статей. Пожалуйста, попробуйте ещё.")

    def handle_article_choice(self, message):
        try:
            page = wikipedia.page(message.text)
            first_paragraph = page.summary.split('\n')[0]
            self.bot.send_message(message.chat.id, first_paragraph)
        except wikipedia.exceptions.DisambiguationError as e:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            for option in e.options:
                markup.add(types.KeyboardButton(option))

            self.bot.send_message(message.chat.id, "Ваш запрос может соответствовать нескольким статьям. Выберите один "
                                                   "из вариантов:", reply_markup=markup)
        except wikipedia.exceptions.PageError:
            self.bot.send_message(message.chat.id, "Извините, статья не найдена. Попробуйте другой запрос.")


if __name__ == "__main__":
    bot = BotStateMachine("TOKEN")
