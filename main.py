def main():
    import telebot
    import var
	from messages import *
	from print_data import *
    import keyboard
    import start_disk
    import transfer


    bot = telebot.TeleBot(var.token_of_bot)

    # Обработка команды /start
    @bot.message_handler(commands=['start'])
    def start_message(msg):
        bot.register_next_step_handler(
            bot.send_message(msg.chat.id, msg_start, reply_markup=keyboard.markup),
            after_start)

	# Обработка сообщения после /start
    def after_start(msg):
        start_disk.main(msg.chat.id,msg.text)

    # Обработка команды /help
    @bot.message_handler(commands=['help'])
    def help_message(msg):
        bot.send_message(msg.chat.id, msg_help)

	# Обработка команды /users
    @bot.message_handler(commands=['users'])
    def users_printin(msg):
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
			
        elif message.text == 'KillTheBotRightNow':
            a = 1 / 0
            print(a)
			
        else:
            bot.send_message(msg.chat.id, msg_help)

	# Транзакция
    def trans(msg):
        print('after trans')
        print('msg:', msg.text, 'id:', msg.chat.id)
        
        def trans_main(msg):
            user = get_user(msg.chat.id)
            if type(user) == dict:
                a = transfer.tr(msg.chat.id, msg.text)   #в конструкторе транзакции происходит проверка
                a.printt()
				
                if a.available_to_trans :
                    if user['Group'] == 'Student':
                        if a.available_to_trans_1:
                            a.main()
                            bot.send_message(msg.chat.id, msg_good_tr)
                    elif user['Group'] == 'Teacher':
                        a.main_teacher()
                        bot.send_message(msg.chat.id, msg_good_tr)
                    else:
                        bot.send_message(msg.chat.id, msg_wrong_st)
                else:
                    bot.send_message(msg.chat.id, msg_wrong_tr)

    try:
        bot.polling(none_stop=True)
    except:
        pass

if __name__ == '__main__':
    main()
