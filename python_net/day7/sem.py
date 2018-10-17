from multiprocessing import Semaphore,Process 
from time import sleep 
import os 
import random

#创建信号量对象 初始为3
sem = Semaphore(3)

def fun():
    print("进程 %d 等待信号量"%os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("进程 %d 消耗了1个信号量"%os.getpid())
    sleep(random.randint(2,5))
    sem.release()
    print("进程 %d 添加了1个信号量"%os.getpid())

jobs = []

for i in range(4):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
