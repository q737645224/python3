
# 1. 用map函数求:
#     1**3 + 2**3 + 3 ** 3 + .... 9**3 的和


s = 0
# 方法1
# for x in range(1, 10):
#     s += x ** 3

#方法2
# for x in map(lambda x: x**3, range(1, 10)):
#     s += x

# 方法3
s = sum(map(lambda x: x**3, range(1, 10)))

print('和是:', s)