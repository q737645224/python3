

# 此示例示意带有形式参数的函数的定义

# 写一个函数，打印出给定的两个数的最大值
def mymax(a, b):
    print('a =', a)
    print('b =', b)
    if a > b:
        print(a, "最大")
    else:
        print(b, '最大')


mymax(100, 200)
mymax("ABC", "123")


