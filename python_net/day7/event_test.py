from multiprocessing import Event 

#创建对象
e = Event()

e.set()  #设置事件

e.wait(5)
print("========================")
print(e.is_set())

e.clear() #清除设置状态
e.wait()