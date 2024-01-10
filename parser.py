from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

html = requests.get('https://hmonline.ru/categories/express-shipping').text
soup = BeautifulSoup(html, 'lxml')

links = soup.find_all('a', class_='products-view-name-link')

data = []
for i, link in enumerate(links):
    url = link.get("href")
    name = link.text
    price = soup.find_all("div", class_="price")[i].text
    data.append([i, url, name, price])

table = tabulate(data, headers=["Index", "URL", "Name", "Price"], tablefmt="grid")
print(table)