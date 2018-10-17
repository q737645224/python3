from socket import * 

sock_file = "./sock"

# 创建套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)
#连接另外一端
sockfd.connect(sock_file)

#发送消息
while True:
    msg = input(">>")
    if msg:
        sockfd.send(msg.encode())
    else:
        break
sockfd.close()