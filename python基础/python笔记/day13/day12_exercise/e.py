# 1. 请编写函数fun 其功能是计算下列多项式的和:
#   fn = 1 + 1/1! + 1/2! + 1/3! + 1/4! + .. + 1/n!
#   (建议用数学模块的factorial实现)
# 求当n 等于100时,fn的值
# 看一下fn(100)的值是什么

import math

# 用循环实现
# def fun(n):
#     s = 0
#     for i in range(0, n + 1):
#         s += 1 / math.factorial(i)  # 1/i!
#     return s

# 用递归实现
def fun(n):
    if n == 0:
        return 1
    return 1 / math.factorial(n) + fun(n - 1)


print(fun(100))  # 2.71828




