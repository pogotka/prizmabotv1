
import telebot
import config

from telebot import types
from string import Template


bot = telebot.TeleBot('1913744856:AAGAOC85HAc9Q-_FFsdZXjgFRT0vz5QIazo')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Магазин')
    btn2 = types.KeyboardButton('О нас')
    btn3 = types.KeyboardButton('Instagram')
    markup.add(btn1, btn2, btn3)
    send_mess = f"Привет, {message.from_user.first_name}!\nВыбери ниже интересующий тебя раздел."
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def bot_msg(message):
    if message.chat.type == 'private':
        if message.text == 'Магазин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('DDD tee')
            btn2 = types.KeyboardButton('UFO tee')
            btn3 = types.KeyboardButton('Назад')
            markup.add(btn1, btn2, btn3)
            send_mess = f"{message.from_user.first_name}, выбери модель футболки."
            bot.send_message(message.chat.id, send_mess, reply_markup=markup)

        elif message.text == 'DDD tee':
            markup = types.InlineKeyboardMarkup()
            photo1 = open('DDDT.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1)
            markup.add(types.InlineKeyboardButton("Перейти в магазин", url="https://toprizma.tb.ru"))
            bot.send_message(message.chat.id, f"<b>DDD tee</b> \n\n100% хлопок \nПрямая печать \nS/M/L \nСтирать при 30 градусах \n\n<b>1290 ₽</b>", parse_mode='html', reply_markup=markup)

        elif message.text == 'UFO tee':
            markup = types.InlineKeyboardMarkup()
            photo2 = open('UFOT.jpg', 'rb')
            bot.send_photo(message.chat.id, photo2)
            markup.add(types.InlineKeyboardButton("Перейти в магазин", url="https://toprizma.tb.ru"))
            bot.send_message(message.chat.id, f"<b>UFO tee</b> \n\n100% хлопок \nПрямая печать \nS/M/L \nСтирать при 30 градусах \n\n<b>1290 ₽</b>", parse_mode='html', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Магазин')
            btn2 = types.KeyboardButton('О нас')
            btn3 = types.KeyboardButton('Instagram')
            markup.add(btn1, btn2, btn3)
            send_mess = f"Выбери ниже интересующий тебя раздел."
            bot.send_message(message.chat.id, send_mess, reply_markup=markup)
        elif message.text == 'О нас':
            bot.send_message(message.chat.id, f'<b>Призма</b> - это творческое объединение, существующее с мая 2020 года. \n\nМы можем сказать много лестных слов о самих себе, но зачем? Призма - такой же бренд, как и Nike, Тинькофф, Apple. Просто они занимаются своими делами, а мы делаем что-то новое. \n\nИнтервью с райтером - сделано! Дроп собственных футболок - сделано! Совершенно новый формат художественных выставок - сделано! А дальше больше. Наша команда стирает границы и не упирается в одну и ту же сферу. Ведь творчество всегда разное, поэтому и мы тоже всегда разные.', parse_mode='html')
            photo3 = open('prizma1.png', 'rb')
            bot.send_photo(message.chat.id, photo3)
        elif message.text == 'Instagram':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Перейти в Instagram", url="https://instagram.com/toprizma"))
            bot.send_message(message.chat.id,
                             f"Нажми на кнопку ниже, чтобы перейти в наш профиль в Instagram",
                             parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id,'Попробуй нажать на кнопку снизу.')


bot.polling(none_stop = True)


























