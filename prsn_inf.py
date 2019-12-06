import var
import json
import os


def info(id):
    us = []
    j = "ahah"
    with open('/home/project/database/users.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            if i["TelegramChatId"] == str(id):
                j = i
                break
    f.close()
    return j
