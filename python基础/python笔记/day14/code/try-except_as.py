# try-except.py


# 此示例示意 try-except 中 as的用法
# as 是用于绑定一个错误对象的变量,
# 可以用此变量得到引发异常的原因

def div_apple(n):
    print("%d个苹果您想分给几个人?" % n)
    s = input("请输入人数: ")
    cnt = int(s)  # <- 此处可能触发ValueError类型错误
    result = n / cnt  # <- 此处可能触发ZeroDivisitionError错误
    print("每个人分了%d个苹果" % result)


try:
    print("开始分苹果")
    div_apple(10)  # 可能触发异常的调用
    print("结束分苹果")
except ValueError as err:
    print("发生成值错误,已处理并转为正常状态!")
    # 要在此处知道错在的原因
    print("错误的原因是: ", err)
except ZeroDivisionError as err:
    print("发生了被零除的错误,程序已转为正常状态")


print("程序正常执行并完全任务,退出程序")


