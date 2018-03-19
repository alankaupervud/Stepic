import requests

with open ('dataset_3378_2.txt') as d:
    url = d.readline().strip()
te = requests.get(url)
print(len (  (te.text).splitlines()) )
