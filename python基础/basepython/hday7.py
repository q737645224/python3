#hday7.py
# seasons = {
#     1:'春季有1,2,3月', 
#     2:'夏季有4,5,6月',
#     3:'秋季有7,8,9月' ,
#     4:'冬季有10,11,12月'
#     }
# i = int(input("输入数字："))
# if i in seasons:
#     print(seasons[i])
# else:
#     print("您输入的数字不在")



# d = dict()
# times = 1
# str_ = input()
# for x in str_:
#     if x not in d:
#         d[x] = times
#     else:
#         d[x] += 1
        
# for k, v in d.items():
#     print(k,":",v)



# L = ['小子','tarena','abc']
# d = {x: len(x) for x in L}
# print(d)

# nos = [1001, 1002, 1005, 1008]
# names = ['tom', 'jerry', 'spike', 'thye']
# d = {nos[index]: names[index] for index in range(len(nos))}
# print(d)   

# d = {}
# for index in range(len(nos)):
#     d[nos[index]] = names[index]
# print(d)

d =dict()
L =list()
while True:
    n = input("请输入姓名：")
    if n == '':
        break
    a = input("请输入年龄：")
    while a == '':
        a = input("请输入年龄：")
    g = input("请输入成绩：")
    while g == '':
        g = input("请输入成绩：")
    d["name"] = n
    d["age"] = a
    d["grade"] = g
    L += [d]
print(L)

print("+" + "-"* 12 + \
    "+" + "-" * 10 + \
    "+" + "-" * 9 + "+")
print("|", "name".center(10), \
    "|", "age".center(8), "|", \
    "grade".center(6), "|" )
print("+" + "-"* 12 + "+" +\
 "-" * 10 + "+" + "-" * 9 + "+")

for i in L:
    n = i["name"]
    a = i["age"]
    g = i["grade"]
print("|", \
    n.center(10), "|", \
    a.center(8), "|", 
    g.center(6), "|" )

print("+" + "-"* 12 + \
    "+" + "-" * 10 + \
    "+" + "-" * 9 + "+")

#模拟电子词典
# d = dict()
# while True:
#     word = input("请输入单词：")
#     if word == "":
#         break
#     explain =input("请数入解释：")
#     d[word] = explain
# index_ =input("输入要查找的单词：")
# if index_ in d:
#     print(d[index_])
# else:
#     print("你输入的单词不存在！")


