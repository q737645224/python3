# exception.py

def f1():
    print("开始盖房子打地基")
    err = ValueError("挖出文物停工")
    return err
    print("地基完成")

def f2():
    print("开始盖房子地上部分")
    print("房子盖完了")

def f3():
    '第二承包商'
    r = f1()
    if r is not None:
        return r
    f2()

def build_house():
    '第一承包商'
    r = f3()
    return r


r = build_house()
print(r)




