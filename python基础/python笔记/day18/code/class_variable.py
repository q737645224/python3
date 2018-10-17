# class_variable.py


class Human:
    total_count = 0  # 类变量

    def __init__(self, name):
        print(name, '对象被创建')


print(Human.total_count)  # 0
h1 = Human('小张')
print(h1.total_count)  # 0 用此类的实例可以访问类变量
h1.total_count = 100  # 为对象添加实例变量
print(h1.total_count)  # 100, 优先访问对象的实例变量
print(Human.total_count)  # 0, 访问类的类变量
h1.__class__.total_count = 12
