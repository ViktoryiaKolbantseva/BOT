import telebot
from telebot import types



bot = telebot.TeleBot('5486937107:AAF_P5BH8b6fag1joSFek8Vy-mo5UvTKAaQ')





@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_tic_tac_toe = types.KeyboardButton('Крестики-Нолики')
    item_calculator = types.KeyboardButton('Калькулятор')
    item_phone_book = types.KeyboardButton('Телефонный справочник')

    markup.add(item_tic_tac_toe, item_calculator, item_phone_book)

    mess = f'Добрый день, {message.from_user.first_name} {message.from_user.last_name}, выбирайте, что будем проверять:)'
    bot.send_message(message.chat.id, mess, reply_markup = markup)





#Первая кнопка с крестиками ноликами


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Крестики-Нолики':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_play = types.KeyboardButton('В мучительной разработке')
        item_menu = types.KeyboardButton('Вернуться в меню')

        markup.add(item_play, item_menu)

        bot.send_message(message.chat.id, 'Хотите сыграть в крестики-нолики?', reply_markup = markup)


# Калькулятор
    elif message.text == 'Калькулятор':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('Мой ID')
        item_username = types.KeyboardButton('Мой ник')
        item_menu = types.KeyboardButton('Вернуться в меню')

        markup.add(item_id, item_username, item_menu)
        bot.send_message(message.chat.id, 'Выбери одну кнопку)', reply_markup=markup)


#Телефонная книга
    elif message.text == 'Телефонный справочник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('В страдательной разработке')
        item_menu = types.KeyboardButton('Вернуться в меню')

        markup.add(item_id, item_menu)
        bot.send_message(message.chat.id, 'Выбери одну кнопку)', reply_markup=markup)



#Вернуться в меню
    elif message.text == 'Вернуться в меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_tic_tac_toe = types.KeyboardButton('Крестики-Нолики')
        item_calculator = types.KeyboardButton('Калькулятор')
        item_phone_book = types.KeyboardButton('Телефонный справочник')

        markup.add(item_tic_tac_toe, item_calculator, item_phone_book)

        mess = f'Что ж, {message.from_user.first_name} {message.from_user.last_name}, давайте выбирать, что будем проверять еще:)'
        bot.send_message(message.chat.id, mess, reply_markup=markup)






bot.polling(none_stop=True)
