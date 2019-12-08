import json

def print_users():
    with open('people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                print(i[j])
                
def print_operations():
    with open(r'../DataBase/operations.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                print(i[j])
                
choice = input()

if choice == '1':
    print_users()
elif choice == '2':
    print_operations()
else:
    print('Некорректный запрос для вывода информации: ', choice)
