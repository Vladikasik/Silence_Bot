import var
import json
import os
import time
from print_data import *

class tr:
	
	def __init__(self,id,msg):

		self.id = id
		self.Username_2, self.transfer_sum = msg.split(' ')
		print(self.Username_2)
		self.balance_1 = 0
		self.balance_2 = 0
		self.available_to_trans = False
		self.data = None
		self.indexes = [0,0]
		self.available_to_trans_1 = False
		self.Username_1 = get_user(self.id)

		sch = 0
		self.data = load_users()
		for user in self.data:
			sch+=1
			if user['TelegramChatId'] == str(self.id):
				self.balance_1 = int(user['Balance'])
				self.indexes[0] = sch
				
			if user['Surname'] == self.Username_2:

				print('Username_2 was found.')

				self.available_to_trans_1 = True
				print('2nd user',self.available_to_trans_1)
				self.balance_2 = int(user['Balance'])
				self.indexes[1] = sch
	
		if int(self.transfer_sum) <= self.balance_1:
			self.available_to_trans = True

	def printt_before(self):
		print('###')
		print('Transf_sum',self.transfer_sum)
		print('Users with their balances before transfer')
		print(self.Username_1, self.Username_2)
		print(self.balance_1,self.balance_2)
		print('###')

	def printt_after(self):
		print('###')
		print('Transf_sum',self.transfer_sum)
		print('Users with their balances after transfer')
		print(self.Username_1, self.Username_2)
		self.balance_1 = get_user(self.id)['Balance']
		self.balance_2 = get_user_by_surname(self.Username_2)['Balance']
		print(self.balance_1,self.balance_2)
		print('###')

	def main(self):

		if self.transfer_sum > 0:
			if self.available_to_trans:
				self.data[self.indexes[0] - 1]['Balance'] = str(
					int(self.data[self.indexes[0] - 1]['Balance']) - int(self.transfer_sum))
				print('Balance 1 was changed')

				self.data[self.indexes[1] - 1]['Balance'] = str(
					int(self.data[self.indexes[1] - 1]['Balance']) + int(self.transfer_sum))
				print('Balance 2 was changed')

				save_users(self.data)

			# не трогайте пж
			with open(r'../database/operations.json', 'r') as f:
				data = json.loads(f.read())
			f.close()

			time1 = time.strftime('%H %M %S %d %m').split()
			time2 = ''
			time3 = [':', ':', '_', '', '']
			for i in range(0, len(time1)):
				time2 += time1[i]
				time2 += time3[i]

			trans_inf = {
				'From: ': self.Username_1,
				'To: ': self.Username_2,
				'Value: ': self.transfer_sum,
				'Time: ': time2
			}
			data.append(trans_inf)

			with open(r'../database/operations.json', 'w') as file:
				json.dump(data, file, indent=2, ensure_ascii=False)
			file.close()

	def main_teacher(self):


		if self.available_to_trans_1:
			self.data[self.indexes[1] - 1]['Balance'] = str(
				int(self.data[self.indexes[1] - 1]['Balance']) + int(self.transfer_sum))
			print('Balance 2 was changed')

			save_users(self.data)

		# не трогайте пж
		with open(r'../database/operations.json', 'r') as f:
			data = json.loads(f.read())
		f.close()

		time1 = time.strftime('%H %M %S %d %m').split()
		time2 = ''
		time3 = [':', ':', '_', '', '']
		for i in range(0, len(time1)):
			time2 += time1[i]
			time2 += time3[i]

		trans_inf = {
			'From: ': self.Username_1,
			'To: ': self.Username_2,
			'Value: ': self.transfer_sum,
			'Time: ': time2
		}
		data.append(trans_inf)

		with open(r'../database/operations.json', 'w') as file:
			json.dump(data, file, indent=2, ensure_ascii=False)
		file.close()





