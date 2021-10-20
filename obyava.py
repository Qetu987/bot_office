import requests
from bs4 import BeautifulSoup

keywords = ['iphone', '11', '64gb']
keyword = '-'.join(keywords)
URL = f'https://obyava.ua/ua/elektronika/telefony-aksessuary/s-{keyword}/'

r = requests.get(URL)
s = BeautifulSoup(r.text, "html.parser")
grid_items = s.find("div", class_="related-list")
items = grid_items.findAll('div', class_='classified-item')


# состаляем список цен
prices = []
for item in items:
    price = item.find("div", class_='classified-price').find("span").text
    price = int(''.join(price[:-4].strip().split(' ')))
    prices.append(price)


# находим среднее
mid = 0
for price in prices:
    mid += price

mid = mid / len(prices)
print(mid)
