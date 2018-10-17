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
    while True:
        sleep(1)
        pid1,status = os.waitpid(-1,os.WNOHANG)
        print(pid1,status)
        if pid1 > 0:
            break 

    while True:
        pass