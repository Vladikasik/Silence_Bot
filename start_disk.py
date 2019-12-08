def main(Id, message):
    import json
    import var
    import os

    print('after /start')
    print('msg:', message, 'id:', Id)
    
    # data = load_users()
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
        file.close()
        
    # добавление ChatId нового пользователя по пригласительному коду
    	for user in data:
            if user['InviteCode'] == message:
                if user['TelegramChatId'] == '':
                    indexx = data.index(user)
                    data[indexx]['TelegramChatId'] = str(Id)
                    print('The new ChatId has been set done.')
                break

    # save_users(data)
    with open('/home/project/database/users.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()
