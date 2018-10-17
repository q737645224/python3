# global4.py


# 4. global变量列表里的变量名不能出现在此作用域的形
#     参列表里
v = 100


def fx(v):
    # global v  # 此处会出错 SyntaxError: name 'v' is parameter and global
    print(v)  # 请问打印多少?


fx(200)
print('v=', v)

