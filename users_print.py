import json
def main():
    with open('/home/project/database/users.json', 'r') as f:
        data = json.loads(f.read())
    f.close()
    strr = ''
    for i in data:
        strr+=str(i)
        strr+='\n'


    return strr
