import requests
from bs4 import BeautifulSoup

url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate10_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate5_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate6_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate9_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate7_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate8_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate11_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/gu_int_rate4_base.html'
#url = 'https://www.nw-life.co.jp/product/annuities/rate/el_int_rate_base3.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data = []
tables = soup.select('.tbl_01-interest')
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

for d in data:
    print(d)
