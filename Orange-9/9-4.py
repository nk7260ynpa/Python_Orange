import requests, re

regex=r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url="http://freetaiwanparty.tw"

html=requests.get(url).text

emails=re.findall(regex,html)
for email in emails:
    print(email)