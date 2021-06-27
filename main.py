from pprint import pprint

import requests
#url = "https://httpbin.org/get"
#resp = requests.get(url)
#print(resp.json())
r = requests.get('https://netology.ru')
#r = requests.get('https://yandex.ru')
pprint(r.text)