import var
import json
import os


def info(id):
    us = []
    j = "ahah"
    print(id)
    with open('/home/project/database/users.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            if i["InviteCode"] == str(id):
                print('info')
                print(i)
                j = i
                break
    f.close()
    return j
