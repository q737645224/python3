from socket import * 
from select import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象
p = poll()

#创建地图
fdmap = {s.fileno():s}

#添加关注
p.register(s,POLLIN | POLLERR)

while True:
    #进行IO监控
    #[(fileno,evnet),...]
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            #从地图中找到fd对应的对象
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #注册新的IO 维护地图
            p.register(c,POLLIN)
            fdmap[c.fileno()] = c 
        else:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd) #从关注移除
                fdmap[fd].close()
                del fdmap[fd]  #从地图删除
            else:
                print(data.decode())
                fdmap[fd].send('收到了'.encode())

