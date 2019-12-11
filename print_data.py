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
        
# загрузка необработанных операций из файла
def load_pending():
    with open(r'../database/pending.json', 'r') as file:
        data = json.loads(file.read())
        file.close()
    return data
    
# сохранение необработанных операций в файл
def save_pending(data):
    with open(r'../database/pending.json', 'w') as file:
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

def get_user_by_surname(surname):
    data = load_users()

    user = ''
    for u in data:
        if u['Surname'] == str(surname):
            user = u
            break

    return user

def str_user(id):
    user = get_user(id)
    if type(user) == dict:
        info = [ user['Name'], ' ', user['Surname'],' (',user['Group'],') ',
                'Баланс: ', user['Balance'], '🥭']

        print(''.join(info))
        return ''.join(info)
    else:
        print('No such user in database.')
        return 'Пользователь не найден в базе. Зарегистрируйтесь с помощью команды /start или обратитесь к администратору.'

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
