# nonlocal.py


# 4. nonlocal语句的变量列表里的变量名，不能出
#     现在此函数的参数列表中
var = 100


def outter():
    var = 200
    print("outter内的var=", var)

    def inner(var):
        nonlocal var  # 此处会出错
        var = 300
        print("inner内的var=", var)
    inner(3)
    print("outter结束时的var=", var)

outter()
print('全局的var=', var)







