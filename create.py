import yadisk
import var
import json

y = yadisk.YaDisk( token = var.token_of_disk )

data = [{'FirstName': 'TestName',
                'SecondName': 'TestSurname',
                'Username': 'test',
                'Balance': '1000',
                'Status': 'Student'}]

file = open( 'people.json', 'w' )

json.dump( data, file, indent=2, ensure_ascii=False )
    
def db():
    y.upload( 'people.json', '/silence_coin/people.json' )

def op():
    y.upload( 'operations.json', '/silence_coin/operations.json' )

a = str(input())

if a == 'op':
    op()
elif a == 'db':
    db()
