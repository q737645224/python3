#二级子进程处理僵尸问题

import os 
from time import sleep

def fun1():
    sleep(3)
    print("第一件事情")

def fun2():
    sleep(4)
    print("第二件事情")

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    #创建二级子进程
    pid1 = os.fork()
    if pid1 == 0:
        fun2() #执行fun2
    elif pid1 > 0:
        os._exit(0) #子进程退出
else:
    os.wait()
    fun1()
    