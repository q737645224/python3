


# 此示例示意函数变量的赋值
def f1():
    print("hello")


def f2():
    print("world")


f1, f2 = f2, f1

f1()  # world
f2()  # hello

