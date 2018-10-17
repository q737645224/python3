# 思考:
#    list类里只有一个append向末尾加一个元素的方法,但没有向列表头部添加元素的方法,试想能否为列表在不改变原有类的基础上添加一个insert_head(n) 方法,实现在列表的头部(前部)添加元素
#   如:
#     class MyList(list):
#         def insert_head(self, n):
#             ...  # 需要自己添加代表

#     myl = MyList(range(3, 6))
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]
#     myl.append(6)
#     print(myl)  # [2, 3, 4, 5, 6]


class MyList(list):
    def insert_head(self, n):
        # ...  # 需要自己添加代表
        # self[0:0] = [n]
        self.insert(0, n)  # 头插


myl = MyList(range(3, 6))
print(myl)  # [3, 4, 5]
myl.insert_head(2)
print(myl)  # [2, 3, 4, 5]
myl.append(6)
print(myl)  # [2, 3, 4, 5, 6]
