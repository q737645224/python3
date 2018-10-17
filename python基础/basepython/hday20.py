# hday20.py
# class A:
#     def __enter__(self):
#         print("diaoyong")    #开始时调用
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):　　　　#结束时
#         print("likai")


# with A() as a:
#     print("zhege")


# class MyNumber:
#     def __init__(self, v):
#         self.data = v
#     def __repr__(self):
#         return  self.data

#     def __add__(self, other):
#         '''此方法用来制定self + other的规则'''
#         v = self.data + other.data
#         return MyNumber(v)  #用v创建一个新的对象返灰给调用者
#     def __sub__(self, rhs):
#         return MyNumber(self.data - rhs.data)

# n1 = MyNumber(100)
# n2 = MyNumber(100)
# # n3 = n1.add(n2)
# n3 = n1 + n2 #可以吗？
# print(n3)


# class Mylist:
#     def __init__(self, iterable=()):
#         self.data = iterable
#     # def __repr__(self):

#     def __add__(self,rhs):
#         print("d")
#         return "Mylist(%s)" %(self.data + rhs.data)
#     def __mul__(self, rhs):
#         return "Mylist(%s)" %(self.data * rhs)
# l1 = Mylist([1, 2, 3])
# l2 = Mylist([4, 5, 6])
# l3 = l1 + l2
# print(l3)  #Mylist([1, 2, 3, 4, 5, 6])
# l3 += l2
# print(l4)
# l5 =l3* 3
# print(l5)
# 
# class Student:
#     def __init__(self, s):
#         self.__score = s

#     def setScore(self, s):
#         if 0 <= s <= 100:
#             self.__score = s

#     def getScore(self):
#         return self.__score

#     @property
#     def score(self):
#         print("getter")
#         return self.__score

#     @score.setter
#     def score(self, s):
#         print("setter")
#         if 0 <= s <= 100:
#             self.__score


# s = Student(50)
# s.score = 11111
# print(s.score)
# # print(s.score)
# s.setScore(100)
# print(s.getScore())

# l = [12, 321]
# l.score =



# 实现有序集合类 OrderSet() 能实现两个集合的交集 &,全集 |,
#   补集 -  对称补集 ^, ==/!= , in/ not in 等操作
#   要求集合内部用 list 存储
# class OrderSet:
#   ...
# s1 = OrderSet([1, 2, 3, 4])
# s2 = OrderSet([3, 4, 5])
# print(s1 & s2)  # OrderSet([3, 4])
# print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])
# if OrderSet([1, 2, 3]) != OrderSet([3, 4, 5]):
#   print("不相等")
# else:
# print("相等")
# if s1 == OrderSet(3, 4, 5):
#  print('s1 == OrderSet(3, 4, 5)')
# if 2 in s1:
#  print("2in s1中返回真")
# ...以下．．

#       方法名               运算符和表达式   说明
#  __and__(self, rhs)        self &  rhs    位与
#  __or__(self, rhs)         self |  rhs    位或
#  __xor__(self, rhs)        self ^  rhs    位异或
 
# __lshift__(self, rhs)     self << rhs    左移
# __rshift__(self, rhs)     self >> rhs    右移
# __invert__(self)          ~ self      取反(一元运算符)

class OrderSet:
    def __init__(self, iterable=[]):
        self.set = set(iterable)
    def __repr__(self):
        l = list(self.set)
        return "OrderSet(%s)" %l
    def __and__(self, rhs):
        return OrderSet(self.set & rhs.set)
    def __or__(self, rhs):
        return OrderSet(self.set | rhs.set)
    def __xor__(self, rhs):
        return OrderSet(self.set ^ rhs.set)
    def __ne__(self,rhs):
        return self.set != rhs.set
    def __eq__(self, rhs):
        return self.set == rhs.set
s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  #OrderSet([3, 4])
print(s1 | s2)
print(s1 ^ s2)
if OrderSet([1, 2, 3]) != OrderSet([3, 4, 5]):
    print("不相等")
else:
    print("相等")
if s1 == OrderSet(3, 4, 5):
    print('s1 == OrderSet(3, 4, 5)')
# if 2 in s1:
#  print("2in s1中返回真")


# print(s1 & s2)  # OrderSet([3, 4])
# print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])
# if OrderSet([1, 2, 3]) != OrderSet([3, 4, 5]):
#   print("不相等")
# else:
# print("相等")
if s1 == OrderSet(3, 4, 5):
 print('s1 == OrderSet(3, 4, 5)')
if 2 in s1:
 print("2in s1中返回真")





