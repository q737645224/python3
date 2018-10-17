# 练习:
#   写一个函数，mymax类似于 内键的函数max
#     详见:
#       >>> help(max)
#    仿造 max 写一信mymax函数，功能与max完全相同
#    (要求不允许调用max函数)
#    print(mymax([6, 8, 3, 5]))  # 8
#    print(mymax(100, 200))  # 200
#    print(mymax(1, 3, 5, 9, 7))  # 9


def mymax(a, *args):
    if len(args) == 0:  # 实参个数等于1时
        zhuida = a[0]
        for x in a:
            if x > zhuida:
                zhuida = x
        return zhuida
    else:  # 实参个数大于1于时
        zhuida = a
        for x in args:
            if x > zhuida:
                zhuida = x
        return zhuida


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))  # 200
print(mymax(1, 3, 5, 9, 7))  # 9
# print(mymax(100))  # 报错

