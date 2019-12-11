import telebot
import var
def tesstt11(msg):
    i = 0
    if msg.text == '909':
        main(msg,i)
def main(msg,i):
    bot = telebot.TeleBot(var.token_of_bot)
    i+=1
    bot.register_next_step_handler(bot.send_message(msg.chat.id,str(i)),
                                                        main(msg,i))
