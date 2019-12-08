import var
import json
import os

def get_user(id):
    user = ""
    
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
        for u in data:
            if u["TelegramChatId"] == str(id):
                user = u
                break
                
    file.close()
    return user
