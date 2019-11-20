import yadisk
import var
y = yadisk.YaDisk(token=var.token_of_disk)
y.upload(r'C:\Users\Vlad\Downloads\people.json','/silence_coin/people.json')