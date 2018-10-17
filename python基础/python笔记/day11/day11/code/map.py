# map.py


# 生成一个可迭代对象，此可迭代对象可以生成1~9自然数的平方
# 1 4 9 16 ..... 81
def power2(x):
    return x ** 2


for x in map(power2, range(1, 10)):
    print(x)  # 1 4 9 16 ....


print('---------------------')
# 生成 1**3 , 2**3, 3**3
def power3(x):
    return x ** 3


for x in map(power3, range(1, 10)):
    print(x)

print('======================')
for x in map(lambda x: x**4, range(1, 10)):
    print(x)



