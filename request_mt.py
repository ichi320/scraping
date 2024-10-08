import csv
from chrome_parser import get_html

#https://www.metlife.co.jp/lf1/ahplf1/top.html


def get_table(soup):
    data = []
    data.append(soup.find('title'))
    tables = soup.select('.defaultTable')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            cols = [col.text.strip() for col in cols]
            data.append(cols)
    return data
#r = requests.get(url)
#soup = BeautifulSoup(r.content, 'html.parser')

def submit():
    url = 'https://www.metlife.co.jp/lf1/ahp664/p664_08.html'
    soup = get_html(url)
    data = []
    data = get_table(soup)
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
    output.append([])

    url = 'https://www.metlife.co.jp/lf1/ahp750/08.html'
    soup = get_html(url, 5)
    data = []
    data = get_table(soup)

    output.append(['ビー ウィズ ユー プラスⅡ'])
    output.append(['健康告知あり'])
    output.append(data[2])
    output.append(data[4])
    output.append(data[5])
    output.append(['健康告知なし'])
    output.append(data[7])
    output.append(data[8])
    output.append(data[9])
    output.append([])


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

if __name__ == '__main__':
    submit()
