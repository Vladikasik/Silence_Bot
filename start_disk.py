def main(id, FirstName, SecondName):
    import json

    import var
    import os

    person_dict = {"Id": str(id),
                   "WebsiteUsername": "",
                   "WebsitePassword": "",
                   "WebsiteSsid": "",
                   "TelegramSurname": str(SecondName),
                   "TelegramName": str(FirstName),
                   "InviteCode": "",
                   "Surname": "",
                   "Name": "",
                   "Balance": "0",
                   "Group": "Student"}

    print(person_dict)
    print('###')
    us = []

    newUser = False

    with open('/home/project/database/people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:


    with open('people.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
