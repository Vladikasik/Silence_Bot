import json
def people():
    with open('people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                print(j)
def operations():
    with open('operations', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                print(j)
a = input()

if a == '1':
    people()
elif a == '2':
    operations()
else:
    print('Идика нахуй')
