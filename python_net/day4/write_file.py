from socket import *
from select import select 
import sys 

s = socket()
s.bind(("127.0.0.1",9999))
s.listen(5)

rlist = [s,sys.stdin]
wlist = []
xlist = []

f = open('file.txt','w')

while True:
    rs,ws,xs = select(rlist,wlist,xlist,3)
    print("***********")
    for r in rs:
        if r is s:
            c,addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin:
            data = r.readline()
            f.write(data) 
            f.flush()
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                f.write(data.decode())
                f.flush()
f.close()
s.close()