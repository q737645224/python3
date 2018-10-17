# return.py


def say_hello():
    print("aaaaaa")
    print("bbbbbb")
    return  # 返回到调用此函数的地方
    print("cccccc")

v = say_hello()

print('v=', v)

say_hello()
