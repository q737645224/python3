# mydeco1.py


# 此示例示意函数装饰器的定义用调用
def mydeco(fn):
    def fx():
        print("=========这是myfunc调用之前==========")
        fn()
        print('---------这是myfunc调用之后----------')
    return fx


@mydeco
def myfunc():
    print("myfunc被调用")


# myfunc = mydeco(myfunc)  # 原理是改变原变量绑定的函数


myfunc()
myfunc()
myfunc()


