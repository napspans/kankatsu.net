##input/local_gov_code.csv 入力データ形式
#   - 全国地方公共団体コード
#     - 422037
#     - 422134
#     - 422142

import pandas as pd
import os

# specified_codes をCSVファイルから読み込む
input_file_path = 'input/local_gov_code.csv'
specified_codes_df = pd.read_csv(input_file_path)
specified_codes = specified_codes_df['全国地方公共団体コード'].tolist()

# mt_town_nagasaki.csv を読み込む（ファイルのパスは適宜調整してください）
file_path = 'input/mt_town_nagasaki.csv'
df = pd.read_csv(file_path)

# 指定された全国地方公共団体コードに該当するデータを抽出
filtered_df = df[df['全国地方公共団体コード'].isin(specified_codes)]

# 指定された全国地方公共団体コードごとのヒット件数を表示
for code in specified_codes:
    count = filtered_df[filtered_df['全国地方公共団体コード'] == code].shape[0]
    print(f"全国地方公共団体コード {code} でヒットした件数: {count}")

# 指定された全国地方公共団体コードに該当するデータを抽出し、明示的にコピーを作成
filtered_df = df[df['全国地方公共団体コード'].isin(specified_codes)].copy()

# "地方公共団体コード(6桁)-町字id(7桁)" のコンビナイドコードを生成
filtered_df.loc[:, 'combined_code'] = filtered_df['全国地方公共団体コード'].astype(str).str.zfill(6) + '-' + filtered_df['町字id'].astype(str).str.zfill(7)

# コンビナイドコードをセミコロン区切りで出力
combined_codes_semicolon = ';'.join(filtered_df['combined_code'].tolist())

# 結果をテキストファイルに保存（必要な場合）
output_path = 'output/combined_codes.txt'
with open(output_path, 'w') as f:
    f.write(combined_codes_semicolon)

# 絶対パスを取得して表示
absolute_path = os.path.abspath(output_path)
print(f"コンビナイドコードが生成されました。\n出力ファイルのリンク: {absolute_path}")
