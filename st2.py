import requests

with open ('dataset_3378_3.txt') as d:
    url = d.readline().strip()

tmp = requests.get(url)
oo = tmp.text
print(oo[:2])


while 'we' not in tmp.text:
    tmp = requests.get(url)
    
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + tmp.text
    print(url)
print(tmp.text)
print(input())﻿
