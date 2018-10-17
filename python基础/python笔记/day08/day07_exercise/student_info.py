# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# 2. 输入任意个学生的姓名，年龄，成绩，每个学生的信息存
#  入字典中，然后放入至列表中，每个学生的信息需要手动输入
# 当输入姓名为空时结束输入:
#   如:
#     请输入姓名:  xiaozhang
#     请输入年龄:  20
#     请输入成绩:  100
#     请输入姓名:  xiaoli
#     请输入年龄:  18
#     请输入成绩:  98
#     请输入姓名:  <回车> 结束输入
#   要求内部存储格式如下:
#   [{'name':'xiaozhang', 'age':20, 'score':100},
#    {'name':'xiaoli', 'age':18, 'score':98}]
#   打印所有学生的信息如下:
#   +---------------+----------+----------+
#   |     name      |   age    |   score  |
#   +---------------+----------+----------+
#   |   xiaozhang   |    20    |   100    |
#   |     xiaoli    |    18    |    98    |
#   +---------------+----------+----------+

L = []  # 创建一个容器准备放入
while True:
    name = input('请输入姓名: ')
    if not name:  # 如果名字为空,结束输入操作
        break
    age = int(input("请输入年龄: "))
    score = int(input("请输入成绩: "))
    d = {}  # 每次都会执行{} 来创建新的字典
    d['name'] = name
    d['age'] = age
    d['score'] = score
    L.append(d)

print(L)

# 打印表格
print("+---------------+----------+----------+")
print("|     name      |   age    |   score  |")
print("+---------------+----------+----------+")
for d in L:
    n = d['name'].center(15)
    a = str(d['age']).center(10)
    s = str(d['score']).center(10)
    print("|%s|%s|%s|" % (n, a, s))

# print("|   xiaozhang   |    20    |   100    |")
# print("|     xiaoli    |    18    |    98    |")
print("+---------------+----------+----------+")
