from multiprocessing import Process,Event 
from time import sleep

def wait_event(file):
    print("准备操作临界资源")
    e.wait()
    print("开始操作临界资源",e.is_set())
    fw = open('1.jpg','wb')
    with open(file,'rb') as f:
        fw.write(f.read())

def wait_event_timeout(file):
    print("也想操作临界资源")
    e.wait(2)
    if e.is_set():
        print("也开始操作临界资源")
        fw = open('2.jpg','wb')
        with open(file,'rb') as f:
            fw.write(f.read())
    else:
        print("等不了了，不等了")

e = Event()
path = "/home/tarena/file.jpg"
file = 'file.jpg'

p1 = Process(target = wait_event,args = (file,))
p2 = Process(target = wait_event_timeout,args = (file,))

p1.start()
p2.start()

print("主进程在操作临界资源")
sleep(3)
fw = open(file,'wb')
with open(path,'rb') as f:
    fw.write(f.read())
fw.close()
e.set()
print("主进程操作完毕")


p1.join()
p2.join()
