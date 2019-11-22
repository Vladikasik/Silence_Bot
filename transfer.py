import yadisk
import var
import json
import os

class tr:


	def __init__(self,Username_1,message):
		self.Username_1 = Username_1
		self.Username_2,self.transfer_sum = message.split()
		self.balance_1 = 0
		self.balance_2 = 0

	def start(self):
		print('shalom')
		y = yadisk.YaDisk(token=var.token_of_disk)
		y.download("/silence_coin/people.json", "people.json")

		with open(r'people.json', 'r') as f:
			data = json.loads(f.read())
			for i in data:
				for j in i:
					if j == 'Username':
						if i['Username'] == self.Username_1:
							self.balance_1 = int(i['Balance'])

		with open(r'people.json', 'r') as f:
			data = json.loads(f.read())
			for i in data:
				for j in i:
					if j == 'Username':
						if i['Username'] == self.Username_2:
							self.balance_2 = int(i['Balance'])
		print(self.Username_1,self.Username_2)
		print(self.balance_1,self.balance_2)
		print('###')