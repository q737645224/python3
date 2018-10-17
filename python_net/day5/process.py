import multiprocessing as mp 
from time import sleep 
import os

a = 1

def fun():
    sleep(2)
    print("子进程事件",os.getpid())
    global a
    a = 10000
    print("a = ",a)

#创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start() 

sleep(3)
print("这是父进程")

#回收进程
p.join()
print("parent a:",a)

# while True:
#     pass
