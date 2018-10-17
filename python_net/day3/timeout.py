from socket import *
import time 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)

#设置套接字的超时检测
s.settimeout(3)

while True:
    print("Waiting from connect...")
    try:
        connfd,addr = s.accept()
    except timeout:
        print("time out....")
        continue

    print("Connect from",addr)
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
    connfd.close()
s.close()