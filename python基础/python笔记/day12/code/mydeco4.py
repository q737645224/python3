# mydeco3.py


# 此示例示意一个函数被两个装饰器先后顺序装饰

def message_send(fn):
    def fy(name, x):
        fn(name, x)
        print(name, "办理了", x, '元的业务![工商银行]')
    return fy


# ----- 以下是小王写的装饰器函数用来进行权限验证----
def privileged_check(fn):
    def fx(name, x):
        print("正在检查权限.... 通过")
        fn(name, x)
    return fx


# ------- 以下是老魏写的程序----------
@privileged_check
def save_money(name, x):  # 存钱
    print(name, '存钱:', x, '元')


@message_send
@privileged_check
def withdraw(name, x):
    print(name, '取钱:', x, '元')


# -------以下是调用者小李写的程序
save_money('小张', 200)
save_money('小赵', 500)
withdraw('小杨', 300)
