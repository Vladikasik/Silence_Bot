import json
a = input('Введит имя')
b = input('Введите фамилию')
c = input('Введите пригласительный код')
d = input('S - student, T - teacher')

with open('/home/project/database/users.json', 'r') as f:
    data = json.loads(f.read())
f.close()

if d == 'S' or d == 's':
    person_dict = {"Id": str(id),
                   "WebsiteUsername": "",
                   "WebsitePassword": "",
                   "WebsiteSsid": "",
                   "InviteCode": c,
                   "Surname": b,
                   "Name": a,
                   "Balance": "0",
                   "Group": "Student"}
    data = data.append(person_dict)
elif d == 'T' or d == 't':
    person_dict = {"Id": str(id),
                   "WebsiteUsername": "",
                   "WebsitePassword": "",
                   "WebsiteSsid": "",
                   "InviteCode": c,
                   "Surname": b,
                   "Name": a,
                   "Balance": "0",
                   "Group": "Teacher"}
    data = data.append(person_dict)





with open('/home/project/database/users.json', 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

file.close()