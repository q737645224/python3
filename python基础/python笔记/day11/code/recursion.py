# recursion.py


def fx(n):
    print("fx进入第", n, '层')
    if n == 3:
        return
    fx(n + 1)
    print("fx退出第", n, '层')


fx(1)
print("程序结束")
