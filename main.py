import telebot
import var
from messages import *
from print_data import *
import keyboard
import transfer
from test11 import *

def main():
    #тут нельзя было импортировать так *
    bot = telebot.TeleBot(var.token_of_bot)
    
##### Обработка команды /start
    @bot.message_handler(commands=['start'])
    def start_message(msg):
        print('/start')
        print('msg:',msg.text,'id:',msg.chat.id)
        bot.register_next_step_handler(
            bot.send_message(msg.chat.id, msg_start, reply_markup=keyboard.markup),
            add_userId)
        
    # Обработка закрытой команды /test
    #@bot.message_handler(commands=['test'])
    #def start_message(msg):
    #    bot.register_next_step_handler(bot.send_message(msg.chat.id,'Введите код'),tesstt11)

    # После команды /start
    def add_userId(msg):
        print('after /start')
        print('msg:', msg.text, 'id:', msg.chat.id)
    
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

##### Обработка команды /help
    @bot.message_handler(commands=['help'])
    def help_message(msg):
        print('/help')
        print('msg:',msg.text,'id:',msg.chat.id)
        bot.send_message(msg.chat.id, msg_help)
        
##### Обработка команды /any
    @bot.message_handler(commands=['any'])
    def any_message(msg):
        print('/any')
        print('msg:',msg.text,'id:',msg.chat.id)
        bot.register_next_step_handler(bot.send_message(msg.chat.id,msg_any),save_any)
        
    def save_any(msg):
        with open('/home/project/database/support.txt','a') as file:
            support_message = str(msg.text) + '\n'
            file.write(support_message)
            file.close()
        bot.send_message(msg.chat.id,msg_any_done)
        #bot.send_message(leo_ivanov_chat_id,msg) #что-нибудь такое получится?
    
##### Обработка команды /approve - только для администратора
    @bot.message_handler(commands=['approve'])
    def approve_message(msg):
        print('/approve')
        print('msg:',msg.text,'id:',msg.chat.id)
        
        pend = load_pending()
        n = len(pend)
        if n > 0:
            t = pend.pop()
            text = 'Транзакция:\n' + str(t) + '\n(Всего: ' + str(n) + ')\nПодтверждаете транзакцию? (Да / Нет / Отложить)'
            bot.register_next_step_handler(
                bot.send_message(msg.chat.id, text, reply_markup=keyboard.markup_admin),
                approve)
        else:
            print('No pending trasactions')
            bot.send_message(msg.chat.id,'Необработанных транзакций нет.')        
        
    def approve(msg):
        print('after approve')
        print('msg:', msg.text, 'id:', msg.chat.id)
        
        admin = get_user(msg.chat.id)
        
        if msg.text == 'Отложить':
            print('Okay, do it later...')
            bot.send_message(msg.chat.id,'Okay, do it later...')
            return        
        
        if (type(admin) != dict) | (admin['Group'] != 'Admin'):
            print('Wrong user')
            bot.send_message(msg.chat.id,'Wrong user')
            return
   
        pend = load_pending()     #загрузить необработанные транзакции
        
        if len(pend) == 0:        #не должно быть
            print('Error len = 0')
            bot.send_message(msg.chat.id,'Error len = 0')
            return

        t = pend.pop()            #взять последнюю транзакцию

        name1 = t['From']
        name2 = t['To']
        value = int(t['Value'])

        user1 = ''
        user2 = ''
        data = load_users()
        for u in data:
            if u['Surname'] == name1:
                 user1 = u
            elif u['Surname'] == name2:
                 user2 = u
            
        if (type(user1) != dict) | (type(user2) != dict):
            print('Wrong users in transaction')
            bot.send_message(msg.chat.id,'Wrong users in transaction')
            return
        
        print(name1,'->',name2)
        print('before:', user1['Balance'], '->', user2['Balance'])
        
        if msg.text == 'Да':
            user2['Balance'] = str(int(user2['Balance']) + value)

            if user1['Group'] == 'Student':
                user1['Balance'] = str(int(user1['Balance']) - value)

            save_pending(pend)
            save_users(data)
            
            print('after:', user1['Balance'], '->', user2['Balance'])
            print('Transaction has been approved.')
            bot.send_message(msg.chat.id,'Transaction has been approved.')
            
        elif msg.text == 'Нет':
            save_pending(pend)
       
            print('Transaction has been declained.')
            bot.send_message(msg.chat.id,'Transaction has been declained.')

    
##### Обработка нажатия кнопок
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
                do_trans)

        elif msg.text == 'KillTheBotRightNow':
            a = 1 / 0
            print(a)

        else:
            bot.send_message(msg.chat.id, msg_help)

    # После команды "Перевод"
    def do_trans(msg):
        print('after trans')
        print('msg:', msg.text, 'id:', msg.chat.id)
        
        user = get_user(msg.chat.id)
        if type(user) == dict:
            a = transfer.trans(msg.chat.id, msg.text)   #в конструкторе транзакции происходит проверка
            a.printt_before()

            if a.user_exists:
                if user['Group'] == 'Student':
                    bot.send_message(msg.chat.id,msg_user_can_not)
                elif (user['Group'] == 'Teacher') | (user['Group'] == 'Admin'):
                    if a.availavle_for_teacher():
                        a.do_teacher()
                        bot.send_message(msg.chat.id, msg_good_tr)
                        a.printt_after()
                    else:
                        bot.send_message(msg.chat.id, msg_wrong_tr)
                else:
                    bot.send_message(msg.chat.id, msg_wrong_st)
            else:
                bot.send_message(msg.chat.id,msg_user_not_exsist)


    try:
        bot.polling(none_stop=True)
    except:
        pass

if __name__ == '__main__':
    main()
