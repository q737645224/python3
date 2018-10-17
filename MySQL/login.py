from mysqlpython import Mysqlpython
from hashlib import sha1

uname = input("请输入用户名:")
pwd = input("请输入密码:")
# 用sha1给pwd加密

s1 = sha1()  # 创建sha1加密对象
s1.update(pwd.encode("utf8"))  # 指定编码
pwd2 = s1.hexdigest()  # 返回16进制加密结果

sqlh = Mysqlpython("db4")
select = "select password from user where \
          username=%s;"
result = sqlh.all(select,[uname])
# print(result)
# (('7c4a8d09ca3762af61e59520943dc26494f8941b',),)

if len(result) == 0:
    print("用户名不存在")
elif result[0][0] == pwd2:
    print("登录成功")
else:
    print("密码错误")

