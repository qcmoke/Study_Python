import pymysql

conn = None

try:
    # 1. 建立连接
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='123456',  # password也可以
                           db='mysql',
                           charset='utf8')  # 如果查询有中文需要指定数据库编码

    if conn is not None:
        print("conn successful !")
        # # 2. 从连接建立游标（有了游标才能操作数据库）
        # cursor = conn.cursor()
        # # 使用execute方法执行SQL语句
        # cursor.execute("SELECT VERSION()")
        # # 使用 fetchone() 方法获取一条数据
        # data = cursor.fetchone()
        # print("Database version : %s " % data)
    else:
        print("conn error !")

except Exception:
    print("连接失败")

finally:
    # 关闭数据库连接
    if conn is not None:
        conn.close()
