import pymysql

# 1.创建数据库连接对象
db = pymysql.connect(host="localhost",user="root",
                password="123456",database="db4",
                charset="utf8")
# 2.创建游标对象
cur = db.cursor()
# 3.执行SQL语句
# 在sheng表中插入1条记录,云南省
try:
    sql_insert = "insert into sheng values\
                  (19,300002,'西藏');"
    cur.execute(sql_insert)
    # 把云南省的 id 号改为 666
    sql_update = "update sheng set id=666 where id=17;"
    cur.execute(sql_update)
    # 把台湾省在 sheng 表中删除
    sql_delete = "delete from sheng where s_name='台湾省';"
    cur.execute(sql_delete)
    print("ok")
    db.commit()
except Exception as e:
    db.rollback()
    print("出现错误,已回滚",e)


# 5.关闭游标对象
cur.close()
# 6.断开数据库连接
db.close()















