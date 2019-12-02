def main():
    import telebot
    import var
    import messages
    import keyboard
    import start_disk
    import prsn_inf
    import transfer

    bot = telebot.TeleBot(var.token_of_bot)
    print(bot)

    # Функйия которая реагирует на команды
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, messages.start_command,reply_markup=keyboard.markup)

        start_disk.main(message.from_user.first_name,
                        message.from_user.last_name,
                         message.from_user.username)

    @bot.message_handler(commands=['help'])
    def help_message(message):
        bot.send_message(message.chat.id,messages.dk)

    # Функция которая реагирует на текст из кнопок
    @bot.message_handler(func=lambda message: True)
    def main_func(message):
        print(message.text)
        if message.text == keyboard.bttn_info:
            per = prsn_inf.info(message.from_user.username)
            mes = messages.inf(per)
            bot.send_message(message.chat.id,mes)
            print('Message sent')
            print('###')
        elif message.text == keyboard.bttn_send:
        # elif message.text == keyboard.bttn_info:
            # mes = bot.send_message(message.chat.id, messages.tr)
            # mes()
            print('else')
            bot.register_next_step_handler\
                    (
                bot.send_message(message.chat.id, messages.tr),
                trans
                    )
        elif message.text == 'KillTheBotRightNow':
            a = 1/0
            print(a)
        else:
            bot.send_message(message.chat.id,messages.dk)


    def trans(mes):
        def trans_main(mes):
            a = transfer.tr(mes.from_user.username, mes.text)
            a.start()
            a.printt()
            a.main()
        def mes_wrong(mes):
            bot.send_message(mes.chat.id,messages.wr)

        mes_massiv = mes.text.split()
        intt = '0123456789'
        correct = False

        if len(mes_massiv) == 2:
            if mes_massiv[0] == str(mes_massiv[0]):
                for i in mes_massiv[1]:
                    if i in intt:
                        correct = True
                    else:
                        correct = False

        if correct:
            trans_main(mes)
            bot.send_message(mes.chat.id,messages.dn)
        else:
            mes_wrong(mes)

    bot.polling()

if __name__ == '__main__':
    main()

