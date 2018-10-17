# myinteger.py


# 此示例示意用生成器函数生成一定范围内的自然数
def myinteger(n):
    i = 0  # 自然数从0开始
    while i < n:
        yield i
        i += 1

for x in myinteger(3):
    print(x)


