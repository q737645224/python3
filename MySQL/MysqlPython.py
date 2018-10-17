from pymysql import connect

class MysqlHelp:
    def __init__(self,database,host="localhost",
                 user="root",password="123456",
                 charset="utf8",port=3306):
        self.database = database
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port

    # 连接数据方法
    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    # 执行SQL语句
    def workOn(self,sql,L=[]):
        self.open()
        try:
            self.cur.execute(sql,L)
            self.conn.commit()
            print("ok")
        except Exception as e:
            self.conn.rollback()
            print("Failed",e)
        self.close()

    # getAll查询方法
    def getAll(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        print("ok")
        result = self.cur.fetchall()
        
        self.close()
        return result

if __name__ == "__main__":
    # 测试
    mysql = MysqlHelp("db4")
    # sql_insert = "insert into sheng(s_name) values('河北省');"
    # mysql.workOn(sql_insert)
    sql_select = "select * from sheng;"
    result = mysql.getAll(sql_select)
    print(result)








