# globals_locals.py


a = 1
b = 2
c = 3


def fn(c, d):
    e = 300
    # 此处有几个局部变量
    print("locals() 返回:", locals())
    print("------------------------")
    print("globals()返回:", globals())
    print("局部变量c的值是:", c)
    print("全局的变量的c的值是:", globals()['c'])


fn(100, 200)
print('===========================')
print("全局的 globals() 返回: ", globals())