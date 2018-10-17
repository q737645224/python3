import os 
from time import sleep,ctime 

while True:
    sleep(2)
    print(ctime(),os.getpid())