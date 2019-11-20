import yadisk
import var
import json

y = yadisk.YaDisk(token=var.token_of_disk)

defoult = [{'FirstName' : 'DefaultTest',
            'SecondName' : 'None',
            'Username': 'test',
            'Balance' : '99999999',
            'Status' : 'Student'}]

with open('people.json', 'w') as file:
    json.dump(defoult, file, indent=2, ensure_ascii=False)

y.upload('people.json','/silence_coin/people.json')