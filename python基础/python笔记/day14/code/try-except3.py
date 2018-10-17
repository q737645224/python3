# try-except.py


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
except ValueError:
    print("苹果不分了,拿回来!")
except:  # 以上没有成功匹配的错误类型在此处都会被捕获
    print("其它的类型的错误,已捕获并转为正常状态")


print("程序正常执行并完全任务,退出程序")
