# constructor.py


# 此示例示意用class 语句创建一个类 Dog
class Dog:
    pass


dog1 = Dog()  # 调用构造函数创建一个实例对象 再用dog1变量绑定
print(id(dog1))
dog2 = Dog()  # 创建另一个实例对象
print(id(dog2))

lst1 = list()  # 创建个列表对象
print(id(lst1))
lst2 = list()  # 创建另一个列表对象
print(id(lst2))

