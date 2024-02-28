import requests
from bs4 import BeautifulSoup
import csv

def get_table(soup):
    data = []
    tables = soup.select('.bordergray00')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            cols = [col.text.strip().replace("\t","").replace("\n","") for col in cols]
            data.append(cols)
    return data

if __name__ == "__main__":
    url = 'https://va-dmn2.nissay.co.jp/vkhengaku/servlet/JP.co.nissay.KE8.KE8S008Z?_gl=1*wulmu6*_gcl_au*MTMxMTY1NjM5NS4xNzA4MzQ3NDA0*_ga*MjA3MDk1NDE4MC4xNzA4MzQ3Mzkw*_ga_R2F88KZ96Y*MTcwODM0NzM4OS4xLjEuMTcwODM0NzQxMC4zOS4wLjA.#GOLD3'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = get_table(soup)
    output = []
    output.append(['一時払終身保険'])
    output.append(['＜ふやすタイプ＞'])
    for i in range(9):
        output.append(data[i])
    output.append([])
    output.append(['＜うけとるタイプ＞'])
    for i in range(9):
        output.append(data[i+9])
    output.append([])
    output.append(['生存給付金付変額保険'])
    for i in range(5):
        output.append(data[i+18])
    output.append([])
    output.append(['生存給付金付特別定期保険'])
    for i in range(7):
        output.append(data[i+23])
    output.append([])
    output.append(['年金原資確定部分付変額年金保険'])
    for i in range(5):
        output.append(data[i+30])

#for d in output:
#    print(d)


    with open('data/nl1.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(output)
