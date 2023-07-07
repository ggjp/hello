# 各行に対して、最初の列はそのまま、それ以外の列を文字列に変換
new_results = [[row[0]] + [str(item) for item in row[1:]] for row in results]

for row in new_results:
    print(row)
