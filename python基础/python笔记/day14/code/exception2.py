# exception.py

def f1():
    print("开始盖房子打地基")
    err = ValueError("挖出文物停工")
    raise err
    print("地基完成")

def f2():
    print("开始盖房子地上部分")
    raise ValueError("要建高压线停工")
    print("房子盖完了")

def f3():
    '第二承包商'
    f1()
    f2()

def build_house():
    '第一承包商'
    f3()


try:
    build_house()
except ValueError as e:
    print(e)




