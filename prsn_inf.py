import yadisk
import var
import json
import os


def info(Username):

    us = []
    with open(r'people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            for j in i:
                if j == 'Username':
                    if i['Username'] == Username:
                        print(i)
                        return i
def dell():
    os.remove('people.json')
                # for k in j:
                #     if k == Username:
                #         while 1:
                #             print('username')
                #         return j