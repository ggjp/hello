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
