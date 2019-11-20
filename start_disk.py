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

    y.download("/silence_coin/people.json", "people.json")
    us = []
    with open('people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                if j == 'Username':
                    us.append(i[j])
        if Username in us:
            data = []
        else:
            pass

    y.remove("/silence_coin/people.json")

    print('data 1',data)
    data.append(person_dict)
    print('data 2', data)

    with open('people.json','w') as file:
        json.dump(data, file, indent=2,ensure_ascii=False)

    y.upload('people.json','/silence_coin/people.json')
    os.remove('people.json')