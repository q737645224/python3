import os 
from time import sleep 

print("******************")
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("This is Child process")
    print("a = ",a)
    a = 10000
else:
    sleep(1)
    print("This is parent process")
    print("parent a :",a)