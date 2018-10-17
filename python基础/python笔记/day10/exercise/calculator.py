# 练习:
#   写一个计算公式的解释执行器
#     已知有如下一些函数：
#         def myadd(x, y):
#             return x + y
#         def mysub(x, y):
#             return x - y
#         def mymul(x, y):
#             return x * y
#     写一个函数，传入字符串，返回相应的函数
#         def get_op(s):
#             # 此函数根据字符串来返回相应的函数.
#             # 如果传入字符串"加" 则返回myadd函数
#             # ....        '乘',则返回mymul函数
#             ... 此处自己实现 
#     主程序如下:
#         while True:
#           s = input("请输入计算公式: ")# 10 加 20
#           L = s.split()
#           a = int(L[0])
#           b = int(L[2])
#           fn = get_op(L[1])
#           print("结果是:", fn(a, b))  # 30




def get_op(s):
    def myadd(x, y):
        return x + y

    def mysub(x, y):
        return x - y

    def mymul(x, y):
        return x * y

    # 此函数根据字符串来返回相应的函数.
    # 如果传入字符串"加" 则返回myadd函数
    # ....        '乘',则返回mymul函数
    if s == '加' or s == '+':
        return myadd
    elif s == '乘' or s == '*':
        return mymul
    elif s == '减' or s == '-':
        return mysub


while True:
    s = input("请输入计算公式: ")  # 10 加 20
    L = s.split()
    a = int(L[0])
    b = int(L[2])
    fn = get_op(L[1])
    print("结果是:", fn(a, b))  # 30
