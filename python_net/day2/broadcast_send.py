from socket import * 
from time import sleep 

#设置广播地址 "<broadcast>"
dest = ('172.60.50.255',9229)

s = socket(AF_INET,SOCK_DGRAM)

#设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("今日立秋".encode(),dest)
s.close()
