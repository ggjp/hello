import psycopg2
from sshtunnel import SSHTunnelForwarder

# トンネル設定
ssh_host = 'your_ssh_host'  # 例: 'ec2-xx-xxx-xxx-xx.compute-1.amazonaws.com'
ssh_username = 'your_ssh_username'  # 通常は 'ec2-user' または 'ubuntu'
ssh_key_path = 'path/to/your/aws_key.pem'  # 例: '/Users/youruser/aws_key.pem'

# PostgreSQL設定
pg_host = 'your_postgresql_host'  # 例: 'your-postgresql-instance.xxxxxxxxxxx.us-east-1.rds.amazonaws.com'
pg_port = 5432
pg_user = 'your_postgresql_username'
pg_password = 'your_postgresql_password'
pg_dbname = 'your_postgresql_dbname'

with SSHTunnelForwarder(
    (ssh_host, 22),
    ssh_username=ssh_username,
    ssh_private_key=ssh_key_path,
    remote_bind_address=(pg_host, pg_port),
) as tunnel:
    conn = psycopg2.connect(
        host='127.0.0.1',
        port=tunnel.local_bind_port,
        user=pg_user,
        password=pg_password,
        dbname=pg_dbname,
    )

    # ここでデータベースの操作を行う
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table_name;')
    results = cursor.fetchall()
    print(results)

    conn.close()
    
# サンプルデータ1
result_list1 = [
    {"store_code": "S001", "product_code": "P001", "price": 100},
    {"store_code": "S001", "product_code": "P002", "price": 200},
]

# サンプルデータ2
result_list2 = [
    {"store_code": "S001", "product_code": "P001", "quantity": 111},
    {"store_code": "S002", "product_code": "P003", "quantity": 300},
]

# 店舗コードと商品コードをキーとしてresult_list2のアイテムを格納する辞書を作成
result_list2_dict = {(item["store_code"], item["product_code"]): item for item in result_list2}

# result_list1のアイテムをベースにresult_list2の一致する商品コードと店舗コードから数量を取得
new_result_list = []
for item in result_list1:
    store_code = item["store_code"]
    product_code = item["product_code"]
    key = (store_code, product_code)
    
    if key in result_list2_dict:
        # result_list2に一致する商品コードと店舗コードがある場合、数量を取得
        item["quantity"] = result_list2_dict[key]["quantity"]
    new_result_list.append(item)

print("New Result List:", new_result_list)


