# global_local.py


# 此示例示意局部变量
a = 100
b = 200


def fx(c):
    d = 400
    a = 100000
    print(a, b, c, d)


fx(300)
print("全局内的", a, b)


