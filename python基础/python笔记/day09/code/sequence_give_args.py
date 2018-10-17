
# position_give_args.py


# 此示例示意位置传参
def myfun1(a, b, c):
    # 这是一个函数的传参示例，此函数以后不会改变代码
    print('a 的值是:', a)
    print('b 的值是:', b)
    print('c 的值是:', c)


s1 = [11, 22, 33]
myfun1(*s1)  # 相当于 myfun1(11, 22, 33)
# myfun1(s1[0], s1[1], s1[2])
t1 = (44, 55, 66)
myfun1(*t1)
myfun1(*"ABC")






