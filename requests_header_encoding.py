import sys
import requests

url = sys.argv[1] if len(sys.argv) > 1 else 'https://www.d-frontier-life.co.jp/products/index_seizon_kyufutsuki_sokuji_shushin_choice.html'
r = requests.get(url)
print(f'encoding: {r.encoding}', file=sys.stderr)
with open('df.html', 'w') as f:
    print(r.text, file=f)
