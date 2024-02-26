from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# coding: UTF-8
def get_html(url):
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

    return soup

if __name__ == '__main__':
    soup = get_html('https://www.google.com/')
    print(soup)
