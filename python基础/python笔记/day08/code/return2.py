# return.py


def say_hello():
    print("aaaaaa")
    print("bbbbbb")
    return [1, 2, 3, 4]  # 返回到调用此函数的地方
    print("cccccc")

v = say_hello()
print('v = ', v)  # None
