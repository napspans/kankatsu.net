# ファイルからデータを読み込む関数
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip().split(';')

# データをファイルに書き込む関数
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(';'.join(data))

# diff_minuend.txt からデータを読み込む
minuend = set(read_file('input/diff_minuend.txt'))

# diff_subtrahend.txt からデータを読み込む
subtrahend = set(read_file('input/diff_subtrahend.txt'))

# 差分を計算する
difference = minuend - subtrahend

# 結果を diff_result.txt に書き込む
write_file('output/diff_result.txt', sorted(list(difference)))
