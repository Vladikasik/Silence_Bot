def main(Id, message):
    import json

    import var
    import os

    # person_dict = {"Id": str(id),
    #                "WebsiteUsername": "",
    #                "WebsitePassword": "",
    #                "WebsiteSsid": "",
    #                "TelegramSurname": str(SecondName),
    #                "TelegramName": str(FirstName),
    #                "InviteCode": "",
    #                "Surname": "",
    #                "Name": "",
    #                "Balance": "0",
    #                "Group": "Student"}

    # print(person_dict)
    # print('###')
    us = []
    done =False
    print('##')
    print('msg:', message.text, 'id:', message.chat.id)
    with open('/home/project/database/users.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            if i['InviteCode'] == message:
                if i['TelegramChatId'] == '':
                    indexx = data.index(i)
                    data[indexx]['TelegramChatId'] = str(Id)
                    mess = 'done'
                    done = True
                else:
                    mess = 'had'

    f.close()
    if done:
        print(mess)

    with open('/home/project/database/users.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()
