from multiprocessing import Process 
from time import sleep 
import os 

def th1():
    sleep(3)
    print("吃饭")
    print(os.getpid(),'---',os.getppid())
def th2():
    sleep(4)
    print("睡觉")
    print(os.getpid(),'---',os.getppid())
def th3():
    sleep(2)
    print("打豆豆")
    print(os.getpid(),'---',os.getppid())

things = [th1,th2,th3]
process = []

for th in things:
    p = Process(target = th)
    process.append(p)  #保存进程对象
    p.start()

#回收进程
for i in process:
    i.join()