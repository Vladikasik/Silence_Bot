import json

# загрузка базы пользователей из файла
def load_users():
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
        file.close()
        return data
    
# сохранение базы пользователей в файл
def save_users(data):
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
        file.close()

# загрузка базы операций из файла
def load_operations):
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
        file.close()
        return data
    
# сохранение базы операций в файл
def save_operations(data):
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
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

def user(id):
	data = load_users()
	
    user = ''
    for u in data:
        if u['TelegramChatId'] == str(id):
            user = u
            break

    return user
