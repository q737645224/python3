# nonlocal2.py

# 3. 当有两层或两层以上函数嵌套时，访问nonlocal变量只
# 对最近的一层变量进行操作


v = 100

def f1():
    v = 200

    def f2():
        v = 300

        def f3():
            nonlocal v
            v = 400
            print('fv3.v=', v)
        f3()
        print("f2.v =", v)
    f2()
    print('f1.v=', v)
f1()

