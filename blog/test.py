import requests

# 配列データ
data = [...] # ここにあなたのデータが入ります

# データを500件ずつに分割
chunks = [data[x:x+500] for x in range(0, len(data), 500)]

# 結果を保存するためのリスト
results = []

# 各チャンクでAPIを呼び出す
for chunk in chunks:
    response = requests.post('http://your-api-url.com', json=chunk)
    if response.status_code == 200:
        results.extend(response.json())
    else:
        print(f"Error: {response.status_code}")
