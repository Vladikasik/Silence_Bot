import json
a = input('Введит имя')
b = input('Введите фамилию')
c = input('Введите пригласительный код')
d = input('S - student, T - teacher')

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

with open('/home/project/database/users.json', 'r') as f:
    data = json.loads(f.read())
f.close()

data = data.append(person_dict)

with open('people.json', 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

file.close()