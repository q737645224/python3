# myyield.py

# 此示例示意生成器函数的定义方法和用法
def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成结束")

gen = myyield()  # gen 绑定一个生成器对象
it = iter(gen)  # 用生成器返回一个迭代器

# 从迭代器获取一个数据(此时生成器函数才开始执行)
print(next(it))




