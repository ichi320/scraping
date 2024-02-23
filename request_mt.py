import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url = 'https://www.metlife.co.jp/lf1/ahp664/p664_08.html'
# coding: UTF-8
# ブラウザのオプションを格納する変数をもらってきます。
options = Options()
# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
options.add_argument("--headless")
# ブラウザを起動する
driver = webdriver.Chrome(options=options)
# ブラウザでアクセスする
driver.get(url)
# HTMLを文字コードをUTF-8に変換してから取得します。
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

#r = requests.get(url)
#soup = BeautifulSoup(r.content, 'html.parser')

data = []
data.append(soup.find('title').string)
tables = soup.select('.defaultTable')
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'span'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

product_names = []
names = soup.select('#H5Exchange01')
for name in names:
    product_names.append(name.text)

output = []
output.append([data[0]])
output.append([product_names[0]])
output.append(data[2])
output.append([product_names[1]])
output.append(data[4])
output.append(data[5])
output.append([product_names[2]])
output.append(data[7])
'''
for d in data:
    print(d)

for pn in product_names:
    print(pn)
'''
#for o in output:
#    print(o)

with open('data/mt1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(output)
