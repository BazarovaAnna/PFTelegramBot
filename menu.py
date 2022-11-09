from telebot import types


def menu(markup):
    itembtnstart = types.InlineKeyboardButton(text='В начало', callback_data='start')
    itembtnpriorities = types.InlineKeyboardButton(text='Посмотреть приоритеты', callback_data='prio')
    itembtninfo = types.InlineKeyboardButton(text='Информация о персонаже', callback_data='info')

    markup.add(itembtnstart)
    markup.add(itembtnpriorities)
    markup.add(itembtninfo)
