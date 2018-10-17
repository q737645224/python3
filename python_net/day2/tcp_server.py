from socket import * 

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('127.0.0.1',9999))

#设置监听
sockfd.listen(5)

while True:
    #等待客户端连接
    print("Waiting for connect...")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)

    while True:
        #消息收发
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive:",data.decode())
        n = connfd.send(b"Receive your message")
        print("send %d bytes"%n)
    #关闭套接字
    connfd.close()

sockfd.close()