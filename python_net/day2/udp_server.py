from socket import * 

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(ADDR)

#消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print("Receive from %s:%s"%(addr,data.decode()))
    sockfd.sendto("收到消息".encode(),addr)

sockfd.close()