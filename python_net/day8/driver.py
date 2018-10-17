from multiprocessing import Process 
import os
from signal import * 
from time import sleep 

def saler_handler(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print("到站了,请下车")
        os._exit(0)

def driver_handler(sig,frame):
    if sig == SIGUSR1:
        print("老司机,开车了")
    elif sig == SIGUSR2:
        print("车速有点快,系好安全带")
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)

#子进程代表售票员
def saler():
    signal(SIGINT,saler_handler) 
    signal(SIGQUIT,saler_handler)
    signal(SIGUSR1,saler_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        sleep(2)
        print("Python带你去远方")


p = Process(target = saler)
p.start()

#父进程
signal(SIGUSR1,driver_handler)
signal(SIGUSR2,driver_handler)
signal(SIGTSTP,driver_handler)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p.join()