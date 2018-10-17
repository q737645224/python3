import pymysql

# 1.创建与数据库连接对象
db = pymysql.connect(host="localhost",user="root",
              password="123456",database="db4",
              charset="utf8")
# 2.利用db方法创建游标对象
cur = db.cursor()

# 3.利用游标对象的execute()方法执行SQL命令
cur.execute("insert into sheng values\
             (16,300000,'台湾省');")

# 4.提交到数据库执行
db.commit()
print("ok")
# 5.关闭游标对象
cur.close()
# 6.断开数据库连接
db.close()

















