import json

a = input('Введите имя ')
b = input('Введите фамилию ')
c = input('Введите пригласительный код ')
d = input('S - student, T - teacher ')

# загружаем текущую базу
with open('/home/project/database/users.json', 'r') as file:
    data = json.loads(file.read())
    file.close()

# добавляем нового пользователя
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

    
# сохраняем новую базу
with open('/home/project/database/users.json', 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()
