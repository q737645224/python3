#tcp_client.py
from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

while True:
    #消息发送接收
    data = input("发送>>")
    if not data:
        break 
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("接受到:",data.decode())

#关闭套接字
sockfd.close()