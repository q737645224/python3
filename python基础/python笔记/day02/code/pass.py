# pass.py

month = int(input("请输入月份: "))
# 如果这个月份在1~12之间，什么事都不做
# 如果不在1~12之间，报错误
if 1 <= month <= 12:
    pass
else:
    print("您的输入有误!")

