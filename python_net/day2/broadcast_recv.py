from socket import * 

#创建数据报套接字
s = socket(AF_INET,SOCK_DGRAM)

#设置套接字可以接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#绑定端口
s.bind(('',9999))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("从{}获取信息：{}".\
            format(addr,msg.decode()))
    except (KeyboardInterrupt,SyntaxError):
        raise 
    except Exception as e:
        print(e)

s.close()
