import os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("Child PID:",os.getpid())
    print("Get parent PID",os.getppid())
else:
    sleep(0.5)
    print("Parent PID:",os.getpid())
    print("Get child PID:",pid)
