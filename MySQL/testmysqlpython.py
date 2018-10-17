from mysqlpython import Mysqlpython

# 创建数据库连接对象
sqlh = Mysqlpython("db4")

# sql_update = "update sheng set s_name='辽宁省' \
#               where s_name='云南省';"
# sqlh.zhixing(sql_update)

sql_select = "select * from sheng where id=%s;"
data = sqlh.all(sql_select,[1])
print(data)






