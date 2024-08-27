import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def get_html(url):
    # coding: UTF-8
    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()
    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.add_argument("--headless")
    # ブラウザを起動する
    driver = webdriver.Chrome(options=options)
    # ブラウザでアクセスする
    driver.get(url)
    #driver.implicitly_wait(10)
    time.sleep(5)

    # HTMLを文字コードをUTF-8に変換してから取得します。
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    return soup

if __name__ == '__main__':
    url = 'https://www.metlife.co.jp/lf1/ahp750/08.html'
    soup = get_html(url)
    print(soup)
