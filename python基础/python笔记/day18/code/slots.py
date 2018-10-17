# slots.py


# 此示例示意 类内的__slots__列表的用法?
class Human:
    # 以下列表限制此类的对象只能有'name' 和'age' 属性
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name, self.age = name, age


h1 = Human("Tarena", 15)
print(h1.age)  # 15
# h1.Age = 18  # 出错,h1对象没有Age属性,也不允许有Age属性
print(h1.age)  # 15

