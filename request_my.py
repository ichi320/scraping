from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from chrome_parser import get_html




def get_table(soup):
    data = []
    data.append([soup.find('title').string])
    tables = soup.select('.rateTable')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            cols = [col.text.strip() for col in cols]
            data.append(cols)
    return data


if __name__ == '__main__':
    url = 'https://www.meijiyasuda.co.jp/window/fc-everybodyplus/rate/'
    soup = get_html(url)

    data = []
    data = get_table(soup)

#    for d in data:
#        print(d)
    with open('data/my1.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
