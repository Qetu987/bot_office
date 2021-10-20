import requests
from bs4 import BeautifulSoup

keywords = ['iphone', '11', '64gb']
keyword = '-'.join(keywords)
URL = f'https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/q-{keyword}/'

r = requests.get(URL)
s = BeautifulSoup(r.text, "html.parser")
u = s.find("div", class_="listHandler")
tables = u.findAll('table', class_='redesigned')

top_taple = tables[1]
items = top_taple.findAll('tr', class_="wrap")

# состаляем список цен
prices = []
for item in items:
    price = item.find('p', class_='price')
    price = price.find('strong').text
    cal = int(''.join(price[:-4].strip().split(' ')))
    prices.append(cal)


# находим среднее
mid = 0
for price in prices:
    mid += price

mid = mid / len(prices)
print(mid)