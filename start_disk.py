def main(FirstName,SecondName,Username):
    import json
    import yadisk
    import var
    import os

    y = yadisk.YaDisk(token=var.token_of_disk)

    person_dict = {'FirstName' : str(FirstName),
                   'SecondName' : str(SecondName),
                   'Username' : Username,
                   'Balance' : '0',
                   'Status' : 'Student'}

    print(person_dict)
    print('###')
    y.download("/silence_coin/people.json", "people.json")
    us = []

    newUser = False

    with open('people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                if j == 'Username':
                    us.append(i[j])
        if Username in us:
            newUser = False
        else:
            newUser = True

    y.remove("/silence_coin/people.json")
    if newUser:
        print('data 1',data)
        data.append(person_dict)
        print('data 2', data)
        print('###')

    with open('people.json','w') as file:
        json.dump(data, file, indent=2,ensure_ascii=False)

    y.upload('people.json','/silence_coin/people.json')
    print('remove')
    os.remove('people.json')
    print('removed')
    print('###')