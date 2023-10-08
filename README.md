# kankatsu.net
kankatsu.netのデータベース作成用リポジトリ

データ整理は```pythonScript```内でpythonコードを書いてデータ生成。

# pythonScript使い方
- [ 諌早市、大村市、東彼杵郡 ]というデータがある場合```local_gov_code_converter.py```を実行し、コンビナイドコードリストまで生成できる。
## 各ファイル
- ```local_gov_code_converter.py```
  - 市町村群のリストから全国地方公共団体コードに変換。
  - [ 諌早市、大村市、東彼杵郡 ] ⇒ [ 422037, 422134, 422142 ]
  - コード出力後 ```filter_data.py```を呼び出し
- ```filter_data.py```
  - 全国地方公共団体コードに一致する大字のコンビナイドコードリストに変換。
  - [ 422037, 422134, 422142 ]csvファイル ⇒ [ 422037-0000101;422037-0000102;422037-0000103; … ]

- ```extract_data_script.py```
  - 〇〇市の内 ××町を抜き出す。
  - 'after_split.txt'の中身
    | 行数 | データ |
    | ---- | ---- |
    | 1行目 | 市町村名 |
    | 2行目以降 | 市町村名 |
# ファイル除外(ignore)
データが100MBを超えるため下記ファイルをコミット除外する。
- ```mt_town_all_withB.csv```
- ```mt_town_all.csv```

必要な場合は下記よりDL
https://drive.google.com/drive/folders/1-Namz__JTsYxFrCRFj0ewt6c-w1gZUr5?usp=sharing


# commit message rules
書き方例``「add:△△を追加」``  
変更を加えて機能を日本語で表記
```
editing: 修正中
add:「～追加」 新しい機能追加
fix:「～修正」 バグの修正
refactor: 「～改善」仕様に影響がないコード改善(リファクタ)
perf:「～向上」 パフォーマンス向上関連
style: コメント等スタイルの修正編集
chore: ビルド、補助ツール、ライブラリ関連
docs: read.me、json、アカウントデータ等ドキュメント修正※
test:「～テスト」 テスト関連
```
※read.me、アカウントデータ等の仕様に影響がないドキュメントはdocumentのブランチにてコミット、マージ