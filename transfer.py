import var
import json
import os
import time
from print_data import *

class trans:

    def __init__(self,id,msg):
		
        self.Username_2 = ' '
        self.transfer_sum = ' '

        text = str(msg)
        if len(text) == 0:
            print('text is empty')
        elif len(text.split(' ')) == 2:
            self.Username_2, self.transfer_sum = text.split(' ')

        self.id = id
        self.balance_1 = 0
        self.balance_2 = 0
        self.available_to_trans = False
        self.available_to_trans_1 = False
        self.indexes = [0,0]
        self.User1 = get_user(self.id)
        self.user_exists = False
        self.data = load_users()
		
        sch = 0
        for user in self.data:
            sch+=1
            if user['TelegramChatId'] == str(self.id):
                self.balance_1 = int(user['Balance'])
                self.indexes[0] = sch
				
            if user['Surname'] == self.Username_2:
                print('Username_2 was found.')
                print('2nd user',self.available_to_trans_1)
                self.user_exists = True
                self.balance_2 = int(user['Balance'])
                self.indexes[1] = sch
	
    def availavle_for_student(self):

        if int(self.transfer_sum) <= self.balance_1 and int(self.transfer_sum) > 0 and self.user_exists :
            self.available_to_trans = True
        else:
            self.available_to_trans = False

        self.transfer_sum_massiv = list(self.transfer_sum)

        intt = '0123456789'

        for item in self.transfer_sum_massiv:
            if item not in intt:
                self.available_to_trans_1 = True
            else:
                self.available_to_trans_1 = False
                break

        return self.available_to_trans and self.available_to_trans_1

    def availavle_for_teacher(self):

        self.available_to_trans = True # у учителей нету ограницения на перевод

        self.transfer_sum_massiv = list(self.transfer_sum)

        intt = '-0123456789'

        for item in self.transfer_sum_massiv:
            if item in intt:
                self.available_to_trans_1 = True
            else:
                self.available_to_trans_1 = False
                break
                
        return self.available_to_trans and self.available_to_trans_1

    def printt_before(self):
        print('### printt_before:')
        print('Transf_sum =',self.transfer_sum)
        print(self.User1['Surname'], self.Username_2)
        print(self.balance_1,self.balance_2)
        print('###')

    def printt_after(self):
        print('### printt_after:')
        print('Transf_sum =',self.transfer_sum)
        print(self.User1['Surname'], self.Username_2)
        self.balance_1 = get_user(self.id)['Balance']
        self.balance_2 = get_user_by_surname(self.Username_2)['Balance']
        print(self.balance_1,self.balance_2)
        print('###')

    def do_student(self):
        #детям нельзя переводить
        return

    def do_teacher(self):
        # добавление транзакции
        time1 = time.strftime('%H %M %S %d %m').split()
        time2 = ''
        time3 = [':', ':', '_', '', '']
        for i in range(0, len(time1)):
            time2 += time1[i]
            time2 += time3[i]

        trans_inf = {
            'From': self.User1['Surname'],
            'To': self.Username_2,
            'Value': self.transfer_sum,
            'Time': time2
        }
		
        data = load_operations()
        data.append(trans_inf)
        save_operations(data)
		
        data = load_pending()
        data.append(trans_inf)
        save_pending(data)
