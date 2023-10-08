###
###〇〇市の内 ××町を抜き出す。
###

# 'after_split.txt'の中身
#
# 1行目:市町村名
# 2行目以降：字名

import pandas as pd
import re

# Specify the path for your CSV and text files here
csv_file_path = 'input/mt_town_nagasaki.csv'
txt_file_path = 'input/after_split.txt'

# Read the CSV file
df = pd.read_csv(csv_file_path)
# Read the first line from 'after_split.txt' to use for filtering
with open(txt_file_path, 'r', encoding='utf-8') as f:
    first_line = f.readline().strip()
# Try filtering by '市区町村名' first
filtered_df = df[df['市区町村名'] == first_line]

# If no matching rows are found, try filtering by '群名'
if filtered_df.empty:
    filtered_df = df[df['郡名'] == first_line]

# Read the text file
with open(txt_file_path, 'r', encoding='utf-8') as f:
    after_split_lines = f.readlines()

# Initialize an empty list to store matched rows as dictionaries
matched_rows = []

# Initialize a list to store unmatched town names
unmatched_towns_corrected = []

# Regular expression to match any non-letter characters (digits, symbols, etc.)
regex = re.compile(r'[^a-zA-Zあ-んア-ン一-龥]')

for idx, town_name in enumerate(after_split_lines):
    town_name = town_name.strip()
    found = False
    cleaned_town_name = regex.split(town_name)[0]
    for column in ['市区町村名','政令市区名', '大字・町名', '丁目名', '小字名']:
        sub_df = filtered_df[filtered_df[column].astype(str).str.startswith(cleaned_town_name)]
        if not sub_df.empty:
            for _, row in sub_df.iterrows():
                combined_code = f"{row['全国地方公共団体コード']}-{str(row['町字id']).zfill(7)};"
                matched_rows.append({
                    '行数': idx + 1,
                    '全国地方公共団体コード': row['全国地方公共団体コード'],
                    '町字id': str(row['町字id']).zfill(7),
                    'combined_code': combined_code,
                    '市区町村名': row['市区町村名'],
                    '大字・町名': row['大字・町名']
                })
            found = True
            break
    if not found:
        unmatched_towns_corrected.append(cleaned_town_name)

# Convert the list of dictionaries to a DataFrame
matched_df_corrected = pd.DataFrame(matched_rows)

# Save the matched DataFrame as a new CSV file
filename_corrected = 'output/' + first_line + '_corrected.csv'
matched_df_corrected.to_csv(filename_corrected, index=False)

# Save the unmatched town names as a text file
filename_uncorrected = 'output/' + first_line + '_uncorrected.txt'
with open(filename_uncorrected, 'w', encoding='utf-8') as f:
    f.write('\n'.join(unmatched_towns_corrected))

# Check if matched_df_corrected is empty
if matched_df_corrected.empty:
    print("全データ該当しませんでした。")
else:
    # Extract 'combined_code' and save it as a text file
    filename_combinedCodeList = 'output/' + first_line + '_combinedCodeList.txt'
    with open(filename_combinedCodeList, 'w', encoding='utf-8') as f:
        f.write(''.join(matched_df_corrected['combined_code'].tolist()))
    print("検出完了しました。")
