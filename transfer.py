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
<<<<<<< Updated upstream
=======
		self.available_to_trans = False
		self.data = None
		self.indexes = [0,0]

>>>>>>> Stashed changes

	def start(self):
		print('shalom')
		self.y = yadisk.YaDisk(token=var.token_of_disk)
		self.y.download("/silence_coin/people.json", "people.json")
		sch = 0
		with open(r'people.json', 'r') as f:
			self.data = json.loads(f.read())
			for i in self.data:
				sch+=1
				print(sch)
				for j in i:
					if j == 'Username':
						if i['Username'] == self.Username_1:
							self.balance_1 = int(i['Balance'])
							self.indexes[0] = sch
		sch = 0
		with open(r'people.json', 'r') as f:
			data = json.loads(f.read())
			for i in data:
				sch+=1
				print(sch)
				for j in i:
					if j == 'Username':
						if i['Username'] == self.Username_2:
							self.balance_2 = int(i['Balance'])
							self.indexes[1] = sch

		available_to_trans = False


<<<<<<< Updated upstream
=======
	def is_available(self):
		if int(self.transfer_sum) <= self.balance_1:
			self.available_to_trans = True

		return self.available_to_trans

>>>>>>> Stashed changes

	def printt(self):
		print(self.Username_1,self.Username_2)
		print(self.balance_1,self.balance_2)

<<<<<<< Updated upstream
		print('###')
=======
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
			self.y.remove('/silence_coin/people.json')
			self.y.upload('people.json', '/silence_coin/people.json')

>>>>>>> Stashed changes
