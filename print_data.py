import json

# загрузка базы пользователей из файла
def load_users():
    with open(r'../database/users.json', 'r') as file:
        data = json.loads(file.read())
        file.close()
    return data
    
# сохранение базы пользователей в файл
def save_users(data):
    with open(r'../database/users.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()

# загрузка базы операций из файла
def load_operations():
    with open(r'../database/operations.json', 'r') as file:
        data = json.loads(file.read())
        file.close()
    return data
    
# сохранение базы операций в файл
def save_operations(data):
    with open(r'../database/operations.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()
        
#######

def print_users():
    with load_users() as data:
        for user in data:
            for info in user:
                print(user[info])
                
def print_operations():
    with load_operations() as data:
        for oper in data:
            for info in oper:
                print(oper[info])

#######

def get_user(id):
    data = load_users()

    user = ''
    for u in data:
        if u['TelegramChatId'] == str(id):
            user = u
            break

    return user

def str_user(id):
    user = get_user(id)
    if type(user) == dict:
        info = ['Имя: ', user['Name'], ' ', user['Surname'], '\n',
                'Id: ', user['TelegramChatId'], '\n',
                'Баланс: ', user['Balance'], '\n',
                'Статус: ', user['Group']]

        print(''.join(info))
        return ''.join(info)
    else:
        print('No such user in database')
        return 'No such user in database'

def str_users():
    data = load_users()

    strr = ''
    for user in data:
        for info in user:
            strr+=str(info)
            strr+=' : '
            strr+=str(user[info])
            strr+='\n'
        strr+='###\n   \n###'
        strr+='\n'
        
    return strr
