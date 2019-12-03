def main(FirstName,SecondName,Username):
    import json
    import yadisk
    import var
    import os


    person_dict = {'FirstName' : str(FirstName),
                   'SecondName' : str(SecondName),
                   'Username' : Username,
                   'Balance' : '0',
                   'Status' : 'Student'}

    print(person_dict)
    print('###')
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


    if newUser:
        print('data 1',data)
        data.append(person_dict)
        print('data 2', data)
        print('###')

    with open('people.json','w') as file:
        json.dump(data, file, indent=2,ensure_ascii=False)


