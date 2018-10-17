from threading import Thread 
from time import sleep 

def fun():
    sleep(3)
    print("Daemon测试")

t = Thread(target = fun)

t.setDaemon(True)
# t.daemon = True

print(t.isDaemon())  #查看daemon值

t.start()

print("======主线程结束======")