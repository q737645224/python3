import pymysql

# 1.创建数据库连接对象
db = pymysql.connect(host="localhost",user="root",
                password="123456",database="db4",
                charset="utf8")
# 2.创建游标对象
cur = db.cursor()

try:
    sql_select = "select * from sheng;"
    cur.execute(sql_select)

    data1 = cur.fetchone()
    print(data1)
    print("*******************")

    data2 = cur.fetchmany(3)
    for m in data2:
        print(m)
    print("*******************")

    data3 = cur.fetchall()
    for m in data3:
        print(m)
    print("*******************")

    db.commit()
except Exception as e:
    print(e)

cur.close()
db.close()

