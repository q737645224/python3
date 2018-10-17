# 练习:
#   已知有一个列表L
#       L = [2, 3, 5, 7]
#     用生成器表达式从此列表中拿到数,生成 列表中数据的平方

#     gen = ......  # 此处用生成器表达式实现
#     L2 = list(gen)  # L2 = [4, 9, 25, 49]


L = [2, 3, 5, 7]


# gen = (x ** 2 for x in L)
def mygen(lst):
    for x in lst:
        yield x ** 2


gen = mygen(L)

L2 = list(gen)  # L2 = [4, 9, 25, 49]
print(L2)
  