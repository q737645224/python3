
# 练习:
#   写一个程序，输入你的出生日期，
#     1) 算出你已经出生多少天?
#     2) 算出你出生的那天是星期几?

import time

year = int(input("请输入出生的年:"))
month = int(input("请输入出生的月:"))
day = int(input("请输入出生的日:"))

# 形成时间元组
tuple_birth = (year, month, day, 0, 0, 0, 0, 0, 0)
# 得到出生时计算机内部秒数
birth_second = time.mktime(tuple_birth)

# 得到一共活了多少秒
second = time.time() - birth_second

print("您已经出生", second/60/60//24, '天')


# 算出生日那天是星期几

t = time.localtime(birth_second)
# print(t)
weeks = {
    0: "星期一",
    1: "星期二",
    2: "星期三",
    3: "星期四",
    4: "星期五",
    5: "星期六",
    6: "星期日"
}


print("您出生的那天是:", weeks[t[6]])
