import os 
from time import sleep 

pid = os.fork()

if pid == 0:
    print("child PID:",os.getpid())
    print("parent PID again:",os.getppid())
elif pid > 0:
    print("parent process:",os.getpid())
    while True:
        pass 
