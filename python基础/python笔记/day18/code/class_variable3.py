# class_variable.py


# 此示例示意类变量的应用
# 用类变量来记录对象的个数

class Human:
    total_count = 0  # 类变量,用来记录实例的个数

    def __init__(self, name):
        print(name, '对象被创建')
        self.__class__.total_count += 1

    def __del__(self):
        '''此方法在对象销毁时,自动将Human.total_count减1'''
        self.__class__.total_count -= 1


h1 = Human('小张')
print('此时Human对象个数是:', Human.total_count)  # 1
L = []
L.append(Human('小李'))
L.append(Human('小赵'))
print('此时Human对象个数是:', Human.total_count)  # 3
del h1  # 删除h1变量,同时解除写'小张'对象绑定关系
L.pop()
print('此时Human对象个数是:', Human.total_count)  # 3





