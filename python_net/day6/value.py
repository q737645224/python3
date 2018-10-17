from  multiprocessing import Process,Value 
import time 
import random  

#创建共享内存
money = Value('i',6000)

#存钱
def deposite():
    for i in range(100):
        time.sleep(0.05)
        #对value的修改就是对共享内存的修改
        money.value += random.randint(1,200)
#花销
def withdraw():
    for i in range(100):
        time.sleep(0.04)
        #对value的修改就是对共享内存的修改
        money.value -= random.randint(1,200)

d = Process(target = deposite)
w = Process(target = withdraw)

d.start()
w.start()

d.join()
w.join()
print(money.value)