
import var
import json
import os
import time

class tr:


	def __init__(self,Username_1,message):

		self.User_1_id = Username_1
		self.Username_2,self.transfer_sum = message.split()
		self.balance_1 = 0
		self.balance_2 = 0
		self.available_to_trans = False
		self.data = None
		self.indexes = [0,0]
		self.available_to_trans_1 = False



	def start(self):
		print('shalom')
		sch = 0
		with open(r'/home/project/database/users.json', 'r') as f:
			self.data = json.loads(f.read())
			for i in self.data:
				sch+=1
				print(sch)
				for j in i:
					if i['TelegramChatId'] == self.User_1_id:
						self.balance_1 = int(i['Balance'])
						self.indexes[0] = sch

		sch = 0
		with open(r'/home/project/database/users.json', 'r') as f:
			data = json.loads(f.read())
			for i in data:
				sch+=1
				print(sch)
				for j in i:
					if i['Surname'] == self.Username_2:
						self.available_to_trans_1 = True
						self.balance_2 = int(i['Balance'])
						self.indexes[1] = sch




	def is_available(self):
		if int(self.transfer_sum) <= self.balance_1 and self.available_to_trans_1:
			self.available_to_trans = True


		return self.available_to_trans


	def printt(self):
		print(self.User_1_id, self.Username_2)
		print(self.balance_1,self.balance_2)

		print('###')

	def main(self):

		if self.is_available():
			self.data[self.indexes[0]-1]['Balance'] = str(
				int(self.data[self.indexes[0]-1]['Balance']) -int(self.transfer_sum))
			print('Balance 1 was changed')

			self.data[self.indexes[1] - 1]['Balance'] = str(
				int(self.data[self.indexes[1] - 1]['Balance']) + int(self.transfer_sum))
			print('Balance 2 was changed')

			with open('people.json', 'w') as file:
				json.dump(self.data, file, indent=2, ensure_ascii=False)

		#не трогайте пж
		with open(r'../database/operations.json', 'r') as f:
			data = json.loads(f.read())
		f.close()
		time1 = time.strftime('%H %M %S %d %m').split()
		time2 = ''
		time3 = [':',':','_','','']
		for i in range(0,len(time1)):
			time2+=time1[i]
			time2 += time3[i]

		trans_inf = {
					'From: ': self.User_1_id,
					'To: ': self.Username_2,
					'Value: ': self.transfer_sum,
					'Time: ': time2
					}
		data.append(trans_inf)
		with open(r'../database/operations.json', 'w') as file:
			json.dump(data, file, indent=2, ensure_ascii=False)
		file.close()




