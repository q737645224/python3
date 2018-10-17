from socket import * 
import os,sys 
from threading import *
import traceback 

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#客户端处理函数
def handler(connfd):
    print("Connect from",connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break 
        print(data.decode())
        connfd.send(b'Receive request')
    connfd.close()

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#等待客户端请求
while True:
    try:
        connfd,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception:
        traceback.print_exc()
        continue 

    t = Thread(target = handler,args = (connfd,))
    t.setDaemon(True)
    t.start()



