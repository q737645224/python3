# class_variable.py


class Human:
    total_count = 0  # 类变量

    def __init__(self, name):
        print(name, '对象被创建')


h1 = Human('小张')
print(Human.total_count)  # 0
h1.__class__.total_count = 100  # 等同于Human.total_count = 100
print(Human.total_count)  # 100


