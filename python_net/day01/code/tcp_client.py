#tcp_client.py 
from socket import * 

#创建套接字 tcp 默认参数即可 
sockfd = socket()

#发起链接请求  #sockfd.accept((ip,端口))
sockfd.connect(('127.0.0.1',8888))

data = input("发送>>")

#发送消息 bytes格式   把消息编码为字节
sockfd.send(data.encode())

data = sockfd.recv(1024).decode()   #接受消息时把字节解码为字符串
print(data)

#关闭套接字
sockfd.close()