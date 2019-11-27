import yadisk
import var
import json

y = yadisk.YaDisk(token=var.token_of_disk)

def db():
    defoult = [{'FirstName': 'DefaultTest',
                'SecondName': 'None',
                'Username': 'vlad_ain',
                'Balance': '99999999',
                'Status': 'Student'}]
    y.remove('/silence_coin/people.json')
    # with open(r'C:\Users\Vlad\Downloads\people.json', 'r') as file:
    #     json.dump(defoult, file, indent=2, ensure_ascii=False)

    y.upload(r'C:\Users\Vlad\Downloads\people.json', '/silence_coin/people.json')

def op():
    y.upload('operations.json','/silence_coin/operations.json')

a = str(input())

if a == 'op':
    op()
elif a == 'db':
    db()