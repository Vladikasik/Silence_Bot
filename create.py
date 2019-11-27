import yadisk
import var
import json

y = yadisk.YaDisk( token = var.token_of_disk )

data = [{'FirstName': 'TestName',
                'SecondName': 'TestSurname',
                'Username': 'test',
                'Balance': '1000',
                'Status': 'Student'}]
    y.remove('/silence_coin/people.json')
    # with open(r'C:\Users\Vlad\Downloads\people.json', 'r') as file:
    #     json.dump(defoult, file, indent=2, ensure_ascii=False)



def op():
    y.upload( 'operations.json', '/silence_coin/operations.json' )

a = str(input())

if a == 'op':
    op()
elif a == 'db':
    db()
