import threading 
import time 
import os 

a = 1 

#线程函数
def music():
    global a 
    a = 10000
    for i in range(5):
        time.sleep(2)
        print("播放葫芦娃",os.getpid())

t = threading.Thread(target = music)
t.start()

for i in range(5):
    time.sleep(1.5)
    print("播放灌篮高手",os.getpid())

t.join()
print("a = ",a)

