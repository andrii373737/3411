import urllib.request
import requests
from bs4 import BeautifulSoup

# response = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features = "html.parser")
#     price_div = soup.find("div", clas = "sc-c1554bc0-0 jgqnJY base-text")
#     if price_div:
#         print(f"Поточна ціна: {price_div.text}")
#     else:
#         print("Не знаходиться")
#

respone = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
respone_text = respone.text
respone_parse = respone_text.split("<span>")
list = []

for e1 in respone_parse:
    if e1.startswith('$'):
        for e2 in e1.split('</span>'):
            if e2.startswith('$') and e2[1].isdigit():
                list.append(e2)
                print(e2)