# -*- coding: utf-8 -*-

import config
import telebot
from telebot import types
from SQLighter import SQLighter
import utils

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['help'])
def print_help_message(message):
    """Метод возвращает описание и список команд"""
    result = 'Ты можешь написать /расписание чтобы посмотреть всё расписание на семестр\nты можешь написать /расписание_на_дату чтобы посмотреть расписание на дату. Дата в формате [гггг-мм-дд]'
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=['расписание'])
def shedule_print(message):
    """Метод возвращает расписание на текущий семестр"""
    db_worker = SQLighter(config.db_name)
    rows = db_worker.select_all()
    result = ''
    for row in rows:
        for elem in row:
            result = result + elem + ', '
        result += '\n'
    bot.send_message(message.chat.id, result)
    db_worker.close()


@bot.message_handler(commands=['расписание_на_дату'])
def shedule_on_day_answer(message):
    """Метод возвращает кастомную клавиатуру с датами"""
    db_worker = SQLighter(config.db_name)
    dates_from_db = db_worker.get_dates()
    dates = []
    for date in dates_from_db:
        dates.append(date[0])
    markup = utils.generate_markup(dates)
    bot.send_message(message.chat.id, 'какая дата?', reply_markup=markup)
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def shedule_on_day_print(message):
    """Метод возвращает расписане на дату"""
    keyboard_hider = types.ReplyKeyboardRemove()
    db_worker = SQLighter(config.db_name)
    date = message.text
    rows = db_worker.get_shedule_on_day(date)
    result = ''
    for row in rows:
        for elem in row:
            result = result + elem + ', '
    bot.send_message(message.chat.id, result, reply_markup=keyboard_hider)

if __name__ == '__main__':
    bot.polling(none_stop=True)