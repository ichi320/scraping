import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.meijiyasuda.co.jp/window/fc-everybodyplus/rate/'
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
tables = soup.select('.rateTable')
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

for d in data:
    print(d)
