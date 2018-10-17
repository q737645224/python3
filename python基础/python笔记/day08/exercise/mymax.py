# 练习:
#   1. 写一个函数 mymax, 给函数传递两个参数，返回两个实参中最大的一个
#     def mymax(a, b):
#          ....

#     v = mymax(100, 200)
#     print('v =', v)  # v = 200
#     print(mymax('ABC', 'abc'))  # abc

# 方法1
# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# 方法2
# def mymax(a, b):
#     if a > b:
#         return a
#     return b

# 方法3
def mymax(a, b):
    return max(a, b)

v = mymax(100, 200)
print('v =', v)  # v = 200
print(mymax('ABC', 'abc'))  # abc
