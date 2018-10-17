from socket import *
import time 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)

#将IO设置为非阻塞
s.setblocking(False)


while True:
    print("Waiting for connect...")

    try:
        c,addr = s.accept()
    except BlockingIOError:
        time.sleep(2)
        print(time.ctime())
        continue

    print("Connect from",addr)
    # c.setblocking(False)
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
    c.close()

s.close()