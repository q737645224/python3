from multiprocessing import Process 
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

p = Process(target = worker,name = "Worker",\
    args = (2,),kwargs = {'name':'Alex'})
p.start()

print(p.name)
print("Child PID:",p.pid) # p进程的进程号
print("is alive?  ",p.is_alive()) #判断进程状态

p.join()
print("is alive?  ",p.is_alive())