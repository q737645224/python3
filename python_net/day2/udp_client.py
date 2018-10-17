from  socket import * 
import sys 

#命令行输入服务器地址
if len(sys.argv) < 3:
    print('''
        argv is error !!
        start as 
        python3 udp_client.py 127.0.0.1 8888
        ''')
    raise 

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("消息：")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print("从服务端收到:",data.decode())

sockfd.close()
