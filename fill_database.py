import json
a = input('Введит имя ')
b = input('Введите фамилию ')
c = input('Введите пригласительный код ')
d = input('S - student, T - teacher ')

with open('/home/project/database/users.json', 'r') as f:
    data = json.loads(f.read())
f.close()

if d == 'S' or d == 's':
    person_dict = {"TelegramChatId": "",
                   "WebsiteUsername": "",
                   "WebsitePassword": "",
                   "WebsiteSsid": "",
                   "InviteCode": c,
                   "Surname": b,
                   "Name": a,
                   "Balance": "0",
                   "Group": "Student"}
    data.append(person_dict)
elif d == 'T' or d == 't':
    person_dict = {"TelegramChatId": "str(id)",
                   "WebsiteUsername": "",
                   "WebsitePassword": "",
                   "WebsiteSsid": "",
                   "InviteCode": c,
                   "Surname": b,
                   "Name": a,
                   "Balance": "0",
                   "Group": "Teacher"}
    data.append(person_dict)




with open('/home/project/database/users.json', 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

file.close()