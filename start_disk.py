from print_data import *

def main(Id, message):
    import json
    import var
    import os

    print('after /start')
    print('msg:', message, 'id:', Id)
    
    data = load_users()
        
    # добавление ChatId нового пользователя по пригласительному коду
    for user in data:
        if user['InviteCode'] == message:
            if user['TelegramChatId'] == '':
                indexx = data.index(user)
                data[indexx]['TelegramChatId'] = str(Id)
                print('The new ChatId has been set done.')
            break

    save_users(data)
