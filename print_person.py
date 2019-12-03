import json
def people():
    with open('people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                print(i[j])
def operations():
    with open('operations', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                print(i[j])
a = input()

if a == '1':
    people()
elif a == '2':
    operations()
else:
    print('Идика нахуй')
