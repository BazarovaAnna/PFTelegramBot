import telebot
from telebot import types

from menu import menu
from pers_controller import get_pers, get_pr_table, get_pr

bot = telebot.TeleBot("5690485734:AAE1iAalmlUN-fcNgEjF82R5fEiTuu18nTI", parse_mode=None)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "start":
        send_welcome(call.message)
    elif call.data == "info":
        work_info(call.message)
    elif call.data == "prio":
        priorities_menu(call.message)
    elif call.data == "prioall":
        bot.send_message(call.message.chat.id, get_pr_table())
    elif call.data == "priop":
        work_prio(call.message)
    elif call.data == "gmstuff":
        master_menu(call.message)
    elif call.data == "rep":
        pass
    elif call.data == "new":
        pass
    elif call.data == "fix":
        pass
    elif call.data == "lvlup":
        pass
    else:
        bot.send_message(call.message.chat.id, "УПС! Эта фича еще на доработке")
        send_welcome(call.message)


# mainmenu = types.InlineKeyboardMarkup()
# key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
# key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
# mainmenu.add(key1, key2)
# bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)


def extract_unique_code(text):
    # Extracts the unique_code from the /start command.
    return text.split()[1] if len(text.split()) > 1 else None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    unique_code = extract_unique_code(message.text)
    markup = types.InlineKeyboardMarkup()
    menu(markup)

    if unique_code == "NmgmHzYFSh" or message.from_user:
        itembtniamgm = types.InlineKeyboardButton(text='Гейм-мастеровы дела', callback_data='gmstuff')
        markup.add(itembtniamgm)

        bot.send_message(message.chat.id, "Ты знаешь, что делать.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Добро пожаловать! Это тестовая версия бота Pathfider Элиния клуба GEEKMO. "
                                          "Некоторые фичи еще прикручиваются, но мы постараемся все "
                                          "сделать хорошо.", reply_markup=markup)


def master_menu(message):
    markup = types.InlineKeyboardMarkup()
    itembtnrep = types.InlineKeyboardButton(text='Отчет по партии', callback_data='rep')
    itembtnnp = types.InlineKeyboardButton(text='Новый персонаж', callback_data='new')
    itembtnfix = types.InlineKeyboardButton(text='Исправить приоритет', callback_data='fix')
    itembtnlvlup = types.InlineKeyboardButton(text='Повысить уровень', callback_data='lvlup')

    markup.add(itembtnrep)
    markup.add(itembtnnp)
    markup.add(itembtnfix)
    markup.add(itembtnlvlup)

    bot.send_message(message.chat.id, "Можно посмотреть приоритет конкретного персонажа, а можно посмотреть "
                                      "всю таблицу с приоритетами - чего пожелаете?", reply_markup=markup)


def priorities_menu(message):
    markup = types.InlineKeyboardMarkup()
    itembtnp1 = types.InlineKeyboardButton(text='Приоритет персонажа', callback_data='priop')
    itembtnpall = types.InlineKeyboardButton(text='Все приоритеты', callback_data='prioall')
    markup.add(itembtnp1)
    markup.add(itembtnpall)

    bot.send_message(message.chat.id, "Можно посмотреть приоритет конкретного персонажа, а можно посмотреть "
                                      "всю таблицу с приоритетами - чего пожелаете?", reply_markup=markup)


def work_info(message):
    bot.send_message(message.chat.id, "Введи имя персонажа, чтобы посмотреть данные о нем.")
    bot.register_next_step_handler(message, get_name)


def work_prio(message):
    bot.send_message(message.chat.id, "Введи имя персонажа, чтобы посмотреть его приоритет.")
    bot.register_next_step_handler(message, get_prio)


def get_name(message):
    name = message.text
    st = get_pers(name)
    bot.send_message(message.chat.id, st)


def get_prio(message):
    name = message.text
    st = get_pr(name)
    bot.send_message(message.chat.id, st)


bot.infinity_polling()
