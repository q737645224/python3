# nonlocal.py


# 此示例示意nonlocal 声明语句的用法
var = 100


def outter():
    var = 200
    print("outter内的var=", var)

    def inner():
        nonlocal var
        var = 300
        print("inner内的var=", var)
    inner()
    print("outter结束时的var=", var)

outter()
print('全局的var=', var)







