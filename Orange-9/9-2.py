import requests

url="http://freetaiwanparty.tw"

html = requests.get(url).text.splitlines()
for i in range(0,15):
    print(html[i])