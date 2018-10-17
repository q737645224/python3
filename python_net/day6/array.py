from multiprocessing import Process,Array
import time 

#创建共享内存
shm = Array('c',b"hello") #字符类型要求是bytes

#开辟5个整形单元的共享内存空间
# shm = Array('i',5)

def fun():
    for i in shm:
        print(i)
    shm[0] = b"H"

p = Process(target = fun)
p.start()
p.join()

print(shm.value) #从首地址打印字符串
# for i in shm:
#     print(i)

