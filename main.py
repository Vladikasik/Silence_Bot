def main():
    import telebot
    import var
    import messages
    import keyboard
    import start_disk
    import prsn_inf
    import transfer
    import users_print

    bot = telebot.TeleBot(var.token_of_bot)


    # Функйия которая реагирует на команды
    @bot.message_handler(commands=['start'])
    def start_message(message):

        bot.register_next_step_handler(
            bot.send_message(message.chat.id, messages.start_command, reply_markup=keyboard.markup),
            st_ds)

    def st_ds(message):
        start_disk.main(message.chat.id,message.text)

    @bot.message_handler(commands=['users'])
    def help_message(message):
        bot.send_message(message.chat.id, messages.dk)

    @bot.message_handler(commands=['start'])
    def users_printin(message):
        bot.send_message(message.chat.id,users_print.main())
    # Функция которая реагирует на текст из кнопок
    @bot.message_handler(func=lambda message: True)
    def main_func(message):
        print(message.text,message.from_user.username)
        if message.text == keyboard.bttn_info:
            per = prsn_inf.info(message.chat.id)
            print(per)
            mes = messages.inf(per)
            bot.send_message(message.chat.id, mes)
        elif message.text == keyboard.bttn_send:
            # elif message.text == keyboard.bttn_info:
            # mes = bot.send_message(message.chat.id, messages.tr)
            # mes()
            bot.register_next_step_handler(
                    bot.send_message(message.chat.id, messages.tr),
                    trans
                                            )
        elif message.text == 'KillTheBotRightNow':
            a = 1 / 0
            print(a)
        else:
            bot.send_message(message.chat.id, messages.dk)

    def trans(mes):

        def trans_main(mes):
            a = transfer.tr(mes.chat.id, mes.text)
            a.start()
            a.printt()

            if a.is_available():
                a.main()
                a.printt()
                bot.send_message(mes.chat.id, messages.dn)
            else:
                mes_wrong(mes)

        def mes_wrong(mes):
            bot.send_message(mes.chat.id, messages.wr)

        mes_massiv = mes.text.split(' ')

        intt = '0123456789'
        correct = False

        if len(mes_massiv) == 2:
            mes_massiv[1] = list(mes_massiv[1])
            for i in mes_massiv[1]:
                if i in intt:

                    correct = True
                else:
                    correct = False
                    break
        sum_masiv = 0
        if correct:
            print('Sum transfer is good')

            for i in mes_massiv[1]:
                sum_masiv += int(i)

        if correct:
            if sum_masiv > 0:
                correct = True
            else:
                correct = False

        if correct:
            print('correct 2')
            trans_main(mes)

        else:
            mes_wrong(mes)

    bot.polling()


if __name__ == '__main__':
    main()
