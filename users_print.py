import json
def main():
    with open('/home/project/database/users.json', 'r') as f:
        data = json.loads(f.read())
    f.close()
    strr = ''
    for i in data:
        for j in i:
            strr+=str(j)
            strr+=' : '
            strr+=str(i[j])
            strr+='\n'
        strr+='###\n   \n###'
        strr+='\n'


    return strr
