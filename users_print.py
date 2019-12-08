import json

def main():
    with open('/home/project/database/users.json', 'r') as file:
        data = json.loads(file.read())
        file.close()

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
