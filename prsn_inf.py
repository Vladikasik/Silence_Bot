
import var
import json
import os


def info(id):

    us = []
    with open('people.json', 'r') as f:
        data = json.loads(f.read())
        for i in data:
            if i["Id"] == str(id):
                print(i)
                return i

def dell():
    os.remove('people.json')
                # for k in j:
                #     if k == Username:
                #         while 1:
                #             print('username')
                #         return j