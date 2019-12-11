import telebot
import var
import time
def tesstt11(msg):
    i = 0
    if msg.text == '909':
        main(msg,i)
def main(msg,i):
    if i < 10:
        bot = telebot.TeleBot(var.token_of_bot)
        i += 1
        bot.register_next_step_handler(bot.send_message(msg.chat.id, 'ok'),
                                       main1(msg,i))

def main1(msg,i):
    print(msg.text)
    main(msg,i)
