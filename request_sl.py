import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import html

url = 'https://neth.sumitomolife.co.jp/neth/A897/A8JA97P101.xhtml'
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
htmldata = driver.page_source.encode('utf-8')
soup = BeautifulSoup(htmldata, 'html.parser')
lxml_data = html.fromstring(str(soup))
tables = lxml_data.xpath('//*[@id="j_id_m"]/div[1]/table/tbody/tr[3]/td/div')

#r = requests.get(url)
#soup = BeautifulSoup(r.content, 'html.parser')

#j_id_m > div:nth-child(2) > table > tbody > tr:nth-child(3) > td > div
#//*[@id="j_id_m"]/div[1]/table/tbody/tr[3]/td/div
data = []
#tables = soup.select('.stTable')

'''まだうまくいっていない。。。'''

print(tables)
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

for d in data:
    print(d)
