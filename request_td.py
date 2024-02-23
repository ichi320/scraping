import requests
from bs4 import BeautifulSoup

url = 'https://www.tdf-life.co.jp/pre_world5/tumitateriritu.html'
url = 'https://www.tdf-life.co.jp/prem_japan5/tumitate_riritu.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data = []
tables = soup.select('.tbl-01')
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

for d in data:
    print(d)
