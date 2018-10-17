# raise.py


def make_exception():
    print("函数开始")
    # 发出一个ValueError类型的错误通知给调用者
    # raise ValueError
    err = ValueError("这是自定义的错误数据")
    raise err  # 用 err触发一个异常通知
    print("函数结束")


try:
    make_exception()
    print("make_exception调用结束!")
except ValueError as e:
    print("接收到ValueError类型的异常通知")
    print("错误对象是:", e)
