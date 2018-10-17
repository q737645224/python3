# function_variable.py


def fa():
    print("hello world")


f1 = fa  # <<<---这里没有括号，f1 变量绑变的是函数
f1()  # 调用 fa绑定的函数
fa()  # 调用 fa绑定的函数

