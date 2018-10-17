from threading import Thread,currentThread
from time import sleep 

#线程函数
def fun(sec):
    print("线程属性测试")
    sleep(sec)
    #获取当前线程对象调用getName()获取名称
    print("%s 线程结束"%currentThread().getName())

thread = []
for i in range(3):
    t = Thread(name = "tedu%d"%i,target = fun,\
        args = (3,))
    thread.append(t)
    t.start()

print(thread[0].is_alive())
thread[1].setName("tarena") #设置线程名称
print(thread[2].name) #获取线程名称

#线程回收
for i in thread:
    i.join()

