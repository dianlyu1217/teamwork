import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('DB_HOST')
db_port = int(os.getenv('DB_PORT'))
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# 创建数据库连接
conn = pymysql.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name,
)


def get_data():
    # 创建游标对象
    cursor = conn.cursor()

    # 执行SQL查询
    cursor.execute("SELECT * FROM product")

    # 获取查询结果
    rows = cursor.fetchall()
    for row in rows:
        print(row)
