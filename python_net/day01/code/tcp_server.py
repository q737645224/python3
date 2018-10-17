#tcp_server.py
from socket import *

#创建tcp套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定IP和端口
sockfd.bind(("127.0.0.1",8888))

#设置监听
sockfd.listen(5)

#等待客户端链接
print("Waiting for connect....")
connfd,addr = sockfd.accept()
print("Connect from",addr)

#接收
data = connfd.recv(1024)
print("Receive message >>",data.decode())

#发送
n = connfd.send(b"Receive your message\n")
print("Send %d bytes data"%n)

#关闭套接字
connfd.close()
sockfd.close()


import socket
sockfd = socket() #建立套接字
sockfd.bind("127.0.0.1",22222) #绑定IP和端口
socket.listen(5)               #创建监听
connfd,addr = sockfd.accept()  #等待客户端链接（IP，端口）匹配
data = connfd.recv(1024)      #接受字节串
n = data = connfd.send()       #发送字节串
connfd.close()                  #关闭套接字2
sockfd.close()