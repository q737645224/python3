from multiprocessing import Process 
from time import sleep,ctime 

def tm1():
    while True:
        sleep(2)
        print(ctime())

p = Process(target = tm1)

p.daemon = True 

p.start()
print("main process over")