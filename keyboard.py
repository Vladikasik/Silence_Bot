from telebot import types

# кнопки для обычного пользователя
bttn_send = '⬆️Перевод'
bttn_info = '🥭Баланс'

markup = types.ReplyKeyboardMarkup()
markup.row(bttn_send)
markup.row(bttn_info)

# кнопки для админа
bttn_yes = 'Да'
bttn_no = 'Нет'
bttn_later = 'Отложить'

markup_admin = types.ReplyKeyboardMarkup()
markup_admin.row(bttn_yes)
markup_admin.row(bttn_no)
markup_admin.row(bttn_later)
