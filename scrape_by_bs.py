from bs4 import BeautifulSoup

with open('df.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

mat = []
table = soup.find('div', class_='box')
mat.append(table.find('p'))
table = soup.find(class_='mb36')
trs = table.find_all('tr')
for tr in trs:
    r = []
    tds = tr.find_all('td')
    for td in tds:
        r.append(td.text)
    mat.append(r)

for m in mat:
    print(m)
