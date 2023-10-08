import pandas as pd
import re
import subprocess

# CSVファイルのパス（この部分は適宜変更してください）
file_path = "input/mt_town_nagasaki.csv"

# CSVファイルを読み込む
df = pd.read_csv(file_path)

# ユーザーに変換する地域名を入力してもらう
input_str = input(">変換する地域を入力してください。")
# 複数の区切り文字で文字列をスプリット
specified_names = re.split(r'[、,。,・]', input_str)

# データフレームから市区町村名と郡名の一覧を取得
city_town_names = df['市区町村名'].unique()
county_names = df['郡名'].dropna().unique()

# すべての一覧に結合
all_names = set(city_town_names) | set(county_names)

# 指定された名前が存在するか確認
found_names = []
not_found_names = []

for name in specified_names:
    if name in all_names:
        found_names.append(name)
    else:
        not_found_names.append(name)

print(f"存在する市町村名または郡名: {', '.join(found_names)}")
print(f"存在しない市町村名または郡名: {', '.join(not_found_names)}")

# 存在する市町村名または郡名に関連する全国地方公共団体コードを抽出
found_codes = df[df['市区町村名'].isin(found_names) | df['郡名'].isin(found_names)]['全国地方公共団体コード'].unique()

# コンマ区切りで出力
print(f"全国地方公共団体コード: {', '.join(map(str, found_codes))}")

# 次のステップの確認
next_step = input(">続いてコンビナイドコードを生成しますか？(y/n)")
if next_step.lower() in ['yes', 'y']:
    # データをCSVに出力
    pd.DataFrame(found_codes, columns=['全国地方公共団体コード']).to_csv('input/local_gov_code.csv', index=False)
    # filter_data_updated_with_temp_file.pyを実行
    subprocess.run(['python', 'filter_data.py'])
