import csv
from chrome_parser import get_html

def get_table(soup):
    data = []
    tables = soup.select('.basic-table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            cols = [col.text.strip() for col in cols]
            data.append(cols)
    return data

def purekare2():
    url = 'https://www.d-frontier-life.co.jp/products/index_choice_23.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append(['プレミアカレンシー・プラス２'])
    output.append(data[0])
    output.append(data[1])
    output.append(data[2])
    output.append(data[3])
    output.append(data[4])
    output.append(data[5])
    output.append(data[6])
    output.append(data[7])
    output.append([])
    return output

def resibu_jpy():
    product_name = 'プレミアレシーブ（円建）'
    url = 'https://www.d-frontier-life.co.jp/products/index_teiki_jpy_23.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    output.append(data[0])
    output.append(data[1])
    output.append(data[2])
    output.append([])
    return output

def resibu_usd():
    product_name = 'プレミアレシーブ（外貨建）'
    url = 'https://www.d-frontier-life.co.jp/products/index_teiki_choice_23.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    output.append(data[0])
    output.append(data[1])
    output.append(data[2])
    output.append(data[3])
    output.append([])
    return output

def resibu2():
    product_name = 'プレミアレシーブ２'
    url = 'https://www.d-frontier-life.co.jp/products/index_recurrining_payment_shushin_23.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(34):
        output.append(data[i])
    output.append([])
    return output

def sutori2():
    product_name = 'プレミアストーリー２'
    url = 'https://www.d-frontier-life.co.jp/products/index_yoro_choice_02.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(15):
        output.append(data[i])
    output.append([])
    return output

def purekare3():
    product_name = 'プレミアカレンシー３'
    url = 'https://www.d-frontier-life.co.jp/products/index_hendo_choice_19_02.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(17):
        output.append(data[i])
    output.append([])
    return output

def jani():
    product_name = 'プレミアジャーニー'
    url = 'https://www.d-frontier-life.co.jp/products/index_hendo_choice_21.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(5):
        output.append(data[i])
    output.append([])
    return output

def sisurendo2():
    product_name = '指数連動年金２'
    url = 'https://www.d-frontier-life.co.jp/products/index_hendo_choice_21_01.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(6):
        output.append(data[i])
    output.append([])
    return output

def purepure3():
    product_name = 'プレミアプレゼント３'
    url = 'https://www.d-frontier-life.co.jp/products/index_hendo_shushin_choice_20_3.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(19):
        output.append(data[i])
    output.append([])
    return output

def sutori4():
    product_name = 'プレミアストーリー４'
    url = 'https://www.d-frontier-life.co.jp/products/index_seizon_kyufutsuki_sokuji_shushin_choice.html'
    soup = get_html(url)
    data = get_table(soup)
    output = []
    output.append([product_name])
    for i in range(46):
        output.append(data[i])
    output.append([])
    return output

def submit():
    with open('data/df1.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(purekare2())
        writer.writerows(resibu_jpy())
        writer.writerows(resibu_usd())
        writer.writerows(resibu2())
        writer.writerows(sutori2())
        writer.writerows(purekare3())
        writer.writerows(jani())
        writer.writerows(sisurendo2())
        writer.writerows(purepure3())
        writer.writerows(sutori4())


if __name__ == '__main__':
#    print(jani())
    submit()
