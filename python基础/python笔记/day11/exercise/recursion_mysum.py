# 练习:
#   写函数 mysum(n)用递归方式实现求和
#     def mysum(n):
#         # 用递归方式求和
#         ...

#     print(mysum(100))  # 5050
#     


def mysum(n):
    if n == 0:
        return 0
    return n + mysum(n - 1)


print(mysum(100))  # 5050
