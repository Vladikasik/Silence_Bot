import var
import json
import os


def info(id):
    us = []
    per = ""
    with open('/home/project/database/users.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            if i["TelegramChatId"] == str(id):
                per = i
                break


    f.close()
    return per
