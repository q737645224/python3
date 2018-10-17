# test_mymod.py


# 此模块为主模块，用于调用mymod模块内的函数
import mymod

mymod.myfac(5)  # 调用自定义模块内的函数
mymod.mysum(10)

print(mymod.name1)  # 使用自定义模块内的数据

name2 = "test_mymod内的name2变量"
print(name2) 
print(mymod.name2)
