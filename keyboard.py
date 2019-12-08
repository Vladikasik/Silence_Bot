from telebot import types

bttn_send = '⬆️Перевод'
bttn_info = '🥭Баланс'

markup = types.ReplyKeyboardMarkup()
markup.row(bttn_send)
markup.row(bttn_info)
