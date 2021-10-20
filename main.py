import requests
from bs4 import BeautifulSoup

class Parser_bot:
    def get_html(self):
        r = requests.get(self.URL)
        return BeautifulSoup(r.text, "html.parser")


    def average(self):
        prices = self.list_price()
        mid = 0
        for price in prices:
            mid += price
        return mid / len(prices)


class Olx_Parser(Parser_bot):
    def __init__(self, keys):
        self.keyword = '-'.join(keys)
        self.URL = f'https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/q-{self.keyword}/'

    
    def get_items(self):
        html = self.get_html()
        item_block = html.find("div", class_="listHandler")
        tables = item_block.findAll('table', class_='redesigned')

        top_taple = tables[1]
        return top_taple.findAll('tr', class_="wrap")

    
    def list_price(self):
        items = self.get_items()
        prices = []
        for item in items:
            price = item.find('p', class_='price')
            price = price.find('strong').text
            cal = int(''.join(price[:-4].strip().split(' ')))
            prices.append(cal)
        return prices


class Obyava_Parser(Parser_bot):
    def __init__(self, keys):
        self.keyword = '-'.join(keys)
        self.URL = f'https://obyava.ua/ua/elektronika/telefony-aksessuary/s-{self.keyword}/'


    def get_items(self):
        html = self.get_html()
        grid_items = html.find("div", class_="related-list")
        return grid_items.findAll('div', class_='classified-item')

    
    def list_price(self):
        items = self.get_items()
        prices = []
        for item in items:
            price = item.find("div", class_='classified-price').find("span").text
            price = int(''.join(price[:-4].strip().split(' ')))
            prices.append(price)
        return prices



a = Olx_Parser(['iphone', '11', '64gb'])
b = Obyava_Parser(['iphone', '11', '64gb'])
print(a.average())
print(b.average())