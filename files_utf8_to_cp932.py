#必要なモジュールをインポート
import glob
from pathlib import Path

#UTF-8、Shift-JISディレクトリへのパス
path_u = Path("./data")
path_s= Path("./data_cp932")

#それぞれのディレクトリで「.csv」が入っている名前のファイルを取得
ufiles = list (path_u.glob("*.csv"))
sfiles = list (path_s.glob("*.csv"))

#UTF-8とShift-JISフォルダの同名ファイルを辞書形式のペアデータとする
files_dict = dict(zip(ufiles,sfiles))

#UTF-8ディレクトリ内のCSVファイルの中身をShift-JISディレクトリ内の同名ファイルに書き込み変換。
#複数ファイルにも対応するようにfor文で書く。cp932=Shift-JIS。replaceはエラーとなった文字を?に置き換え。
for ufile,sfile in files_dict.items():#.items()は辞書形式のデータでfor文をまわす際によく利用します。
    with open(ufile, encoding='utf-8',errors='replace') as fin:
        with open(sfile, 'w', encoding='cp932',errors='replace') as fout:
            fout.write(fin.read())