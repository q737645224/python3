import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("create process faild")
elif pid == 0:
    print("Child process running")
    sleep(3)
    print("Child process over")
    os._exit(3)
else:
    #等子进程执行完毕进行回收
    pid,status = os.wait()
    print(pid,status)
    print(os.WEXITSTATUS(status)) #原来退出状态
    while True:
        pass