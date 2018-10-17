# global.py


v = 100


def fn():
    global v  # 声明v是全局，此时不允许在此作用域存在v
    v = 200  # 想让此语句去修改全局作用域内的变量v
    print('fn内的v =', v)


fn()
print("v=", v)  # 100