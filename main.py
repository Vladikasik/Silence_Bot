import telebot
import var
from messages import *
from print_data import *
import keyboard
import transfer
from datetime import datetime

#список спаммеров - в дальнейшем нужно автоматизировать и считывать из файла, если нужно, но чтобы не перегружать работу бота
block_user = {
    872683288: datetime(2019, 12, 21),   #блокировка Давида до 21.12.2019
}

def main():
    bot = telebot.TeleBot(var.token_of_bot)
    
    def print_log(msg):
        print('[' + strftime('%x %X') + ' >> ' + str(msg.chat.id) + ']:')
        print('msg:',msg.text)
    
##### Обработка команды /start
    @bot.message_handler(commands=['start'])
    def start_message(msg):
        print_log(msg)
        bot.register_next_step_handler(
            bot.send_message(msg.chat.id, msg_start, reply_markup=keyboard.markup),
            add_userId)
        
    # После команды /start
    def add_userId(msg):
        print_log(msg)
    
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
        print_log(msg)
        bot.send_message(msg.chat.id, msg_help)
        
##### Обработка команды /any
    @bot.message_handler(commands=['any'])
    def any_message(msg):
        print_log(msg)
        bot.register_next_step_handler(bot.send_message(msg.chat.id,msg_any),save_any)
        
    def save_any(msg):
        with open('/home/project/database/support.txt','a') as file:
            support_message = str(msg.text) + '\n'
            file.write(support_message)
            file.close()
        bot.send_message(msg.chat.id,msg_any_done)
        #bot.send_message(var.support_telegram_id,msg.text) #отправка сообщения специально выделенному контакту

##### Обработка команды /approve - только для администратора
    @bot.message_handler(commands=['approve'])
    def approve_message(msg):
        print_log(msg)
        
        admin = get_user(msg.chat.id)
        
        if type(admin) != dict:
            print('User data error')
            bot.send_message(msg.chat.id,'Ошибка данных пользователя.')
            return
        elif admin['Group'] != 'Admin':
            print('No admin permission')
            bot.send_message(msg.chat.id,'Недостаточно прав. Команда доступна только администратору.')
            return    
        
        pend = load_pending()
        n = len(pend)
        if n > 0:
            t = pend.pop()
            text = 'Транзакция:\n' + str(t) + '\n(Всего: ' + str(n) + ')\nПодтверждаете транзакцию?\n(Да / Нет / Отложить)'
            print(text)
            bot.register_next_step_handler(
                bot.send_message(msg.chat.id, text, reply_markup=keyboard.markup_admin),
                approve)
        else:
            print('No pending trasactions')
            bot.send_message(msg.chat.id,'Необработанных транзакций нет.')        
        
    def approve(msg):
        print_log(msg)
        
        admin = get_user(msg.chat.id)
        
        if msg.text == 'Отложить':
            print('Okay, do it later...')
            bot.send_message(msg.chat.id,'Обработка транзакции отложена.', reply_markup=keyboard.markup)
            return              
   
        pend = load_pending()     #загрузить необработанные транзакции
        
        if len(pend) == 0:        #не должно быть
            print('Error len = 0')
            bot.send_message(msg.chat.id,'Error len = 0', reply_markup=keyboard.markup)
            return

        t = pend.pop()            #взять последнюю транзакцию

        if msg.text == 'Нет':
            save_pending(pend)

            print('Transaction has been declained.')
            bot.send_message(msg.chat.id,'Транзакция успешно отклонена.', reply_markup=keyboard.markup)
            
        elif msg.text == 'Да':
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
                print('User data error in transaction')
                bot.send_message(msg.chat.id,'User data error in transaction', reply_markup=keyboard.markup)
                return
            
            if name1 == name2:
                print('Same user error in transaction')
                bot.send_message(msg.chat.id,'Нельзя осуществлять перевод самому себе.', reply_markup=keyboard.markup)
                return    
            
            print(name1,'->',name2)
            print('before:', user1['Balance'], '->', user2['Balance'])
            
            # здесь происходит основной перевод! -------------------------
            user2['Balance'] = str(int(user2['Balance']) + value)

            if user1['Group'] == 'Student':
                user1['Balance'] = str(int(user1['Balance']) - value)
            # ------------------------------------------------------------
            
            save_pending(pend)
            save_users(data)
            
            print('after:', user1['Balance'], '->', user2['Balance'])
            print('Transaction has been approved.')
            
            # текст сообщения для пользователя 2
            text = str() + user1['Surname'] + user1['Name']
            text += ' снял(а) с Вас ' if (value < 0) else ' перевел(а) Вам '
            text += str(abs(value)) + '🥭.'
            
            bot.send_message(int(user2['TelegramChatId']), text, reply_markup=keyboard.markup)
            bot.send_message(msg.chat.id, 'Транзакция успешно подтверждена.', reply_markup=keyboard.markup)

    
##### Обработка всех остальных сообщений или кнопок
    @bot.message_handler(func=lambda msg: True)
    def main_func(msg):
        #проверка по спам-списку
        block_date = block_user.get( msg.chat.id )
        if block_date != None:
            if datetime.now() < block_date:
                return  #если дедлайн блокировки юзера не прошел, то не обрабатываем сообщение

        print_log(msg)

        # Обработка нажатия кнопки "Баланс"
        if msg.text == keyboard.bttn_info:
            bot.send_message(msg.chat.id, str_user(msg.chat.id))

        # Обработка нажатия кнопки "Перевод"
        elif msg.text == keyboard.bttn_send:
            bot.register_next_step_handler(
                bot.send_message(msg.chat.id, msg_trans),
                do_trans)

        elif msg.text == 'KillTheBotRightNow':
            bot.send_message(msg.chat.id, 'Вы убили бота. Ни одно живое существо не пострадало.')
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
