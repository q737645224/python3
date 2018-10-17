

# 生成一个可迭代对象，此可迭代对象可以生成:
#   1**4,  2**3,  3**2,  4**1
def power_a_b(a, b):
    return a ** b


for x in map(power_a_b,
             [1, 2, 3, 4, 5, 6, 7, 8],
             [4, 3, 2, 1]):
    print(x)

