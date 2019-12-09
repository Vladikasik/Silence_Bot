import telebot
import var
from messages import *
from print_data import *
import keyboard
import start_disk
import transfer
def main():
    #тут нельзя было импортировать так *
    bot = telebot.TeleBot(var.token_of_bot)

    # Обработка команды /start
    @bot.message_handler(commands=['start'])
    def start_message(msg):
        print('/start')
        print('msg:',msg.text,'id:',msg.chat.id)
        bot.register_next_step_handler(
            bot.send_message(msg.chat.id, msg_start, reply_markup=keyboard.markup),
            add_userId)

    # После команды /start
    def add_userId(msg):
        print('after /start')
        print('msg:', msg, 'id:', msg.chat.id)
    
        data = load_users()

        for user in data:# добавление ChatId нового пользователя по пригласительному коду
            if user['InviteCode'] == msg.text:
                if user['TelegramChatId'] == '':
                    indexx = data.index(user)
                    data[indexx]['TelegramChatId'] = str(msg.chat.id)
                    print('The new ChatId has been set done.')
                    bot.send_message(msg.chat.id,msg_done_id)
                break
        save_users(data)

    # Обработка команды /help
    @bot.message_handler(commands=['help'])
    def help_message(msg):
        print('/help')
        print('msg:',msg.text,'id:',msg.chat.id)
        bot.send_message(msg.chat.id, msg_help)

    # Обработка команды /users
    @bot.message_handler(commands=['users'])
    def users_message(msg):
        print('/users')
        print('msg:',msg.text,'id:',msg.chat.id)
        bot.send_message(msg.chat.id,str_users())
    
    # Обработка нажатия кнопок
    @bot.message_handler(func=lambda msg: True)
    def main_func(msg):
        print('button')
        print('msg:',msg.text,'id:',msg.chat.id)

        # Обработка нажатия кнопки "Баланс"
        if msg.text == keyboard.bttn_info:
            bot.send_message(msg.chat.id, str_user(msg.chat.id))

        # Обработка нажатия кнопки "Перевод"
        elif msg.text == keyboard.bttn_send:
            bot.register_next_step_handler(
                bot.send_message(msg.chat.id, msg_trans),
                trans)

        elif msg.text == 'KillTheBotRightNow':
            a = 1 / 0
            print(a)

        else:
            bot.send_message(msg.chat.id, msg_help)

    # После команды "Перевод"
    def trans(msg):
        print('after trans')
        print('msg:', msg.text, 'id:', msg.chat.id)
        
        user = get_user(msg.chat.id)
        if type(user) == dict:
            a = transfer.tr(msg.chat.id, msg.text)   #в конструкторе транзакции происходит проверка
            a.printt_before()

            # if a.available_to_trans :
            #     if user['Group'] == 'Student':
            #         if a.available_to_trans_1:
            #             a.main()
            #             bot.send_message(msg.chat.id, msg_good_tr)
            #     elif user['Group'] == 'Teacher':
            #         a.main_teacher()
            #         bot.send_message(msg.chat.id, msg_good_tr)
            #     else:
            #         bot.send_message(msg.chat.id, msg_wrong_st)
            # else:
            #     bot.send_message(msg.chat.id, msg_wrong_tr)

            if user['Group'] == 'Student':
                if a.availavle_for_student():
                    a.main_student()
                    bot.send_message(msg.chat.id,msg_good_tr)
                    a.printt_after()
                else:
                    bot.send_message(msg.chat.id,msg_wrong_tr)
            elif user['Group'] == 'Teacher':
                if a.availavle_for_teacher():
                    a.main_teacher()
                    bot.send_message(msg.chat.id,msg_good_tr)
                    a.printt_after()
                else:
                    bot.send_message(msg.chat.id,msg_wrong_tr)
            else:
                bot.send_message(msg.chat.id,msg_wrong_st)



    try:
        bot.polling(none_stop=True)
    except:
        pass

if __name__ == '__main__':
    main()
