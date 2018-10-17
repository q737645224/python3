
# position_give_args.py


# 此示例示意位置传参
def myfun1(a, b, c):
    # 这是一个函数的传参示例，此函数以后不会改变代码
    print('a 的值是:', a)
    print('b 的值是:', b)
    print('c 的值是:', c)


d = {'a': 100, 'b': 200, 'c': 300}
myfun1(**d)  # 等同于 myfun1(a=100,b=200,c=300)

# 下是错误做法
# d2 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
# myfun1(**d2)

