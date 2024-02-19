import requests
from bs4 import BeautifulSoup

url = 'https://va-dmn2.nissay.co.jp/vkhengaku/servlet/JP.co.nissay.KE8.KE8S008Z?_gl=1*wulmu6*_gcl_au*MTMxMTY1NjM5NS4xNzA4MzQ3NDA0*_ga*MjA3MDk1NDE4MC4xNzA4MzQ3Mzkw*_ga_R2F88KZ96Y*MTcwODM0NzM4OS4xLjEuMTcwODM0NzQxMC4zOS4wLjA.#GOLD3'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data = []
tables = soup.select('.bordergray00')
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

for d in data:
    print(d)
