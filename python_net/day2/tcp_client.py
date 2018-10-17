from socket import * 

#创建套接字
sockfd = socket()

#发起连接
sockfd.connect(('127.0.0.1',9999))

while True:
    #消息收发
    msg = input("Msg>>")
    if not msg:
        break
    sockfd.sendall(msg.encode())
    data = sockfd.recv(1024)
    print(data.decode())

sockfd.close()