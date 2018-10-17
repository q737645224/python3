from socket import * 
from select import select 

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    print("等待IO发生")
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            connfd,addr = r.accept()
            print("Connect from",addr)
            rlist.append(connfd)
        #表示客户端连接套接字准备就绪
        else:
            data = r.recv(1024)
            if not data:
                #从关注列表移除
                rlist.remove(r)
                r.close()
            else:    
                print("Receive:",data.decode())
                #讲客户端套接字放入wlist
                wlist.append(r)
    for w in ws:
        w.send("这是一条回复消息".encode())
        wlist.remove(w)
    for x in xs:
        if x is s:
            s.close()