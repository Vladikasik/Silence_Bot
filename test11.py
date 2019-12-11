import telebot
import var
import time
def tesstt11(msg):
    i = 0
    if msg.text == '909':
        main(msg,i)
def main(msg,i):
    if i < 10:
        lol = msg.text
        bot = telebot.TeleBot(var.token_of_bot)
        i += 1
        bot.register_next_step_handler(bot.send_message(msg.chat.id, lol),
                                       main(msg,i))
        time.sleep(2)
    else:
        print('done')
