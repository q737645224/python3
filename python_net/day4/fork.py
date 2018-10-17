import  os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("创建进程失败")

#子进程执行部分
elif pid == 0:
    print("新进程创建成功")

#父进程执行部分
else:
    sleep(1)
    print("原来的进程")

print("程序执行完毕")