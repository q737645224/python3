from socket import * 

s = socket()

s.connect(('172.60.50.181',8888))

filename = s.recv(1024).decode()

f = open('/home/tarena/'+filename,'wb')

while True:
    data = s.recv(1024)
    if data == b'##':
        break
    f.write(data)

s.send("接收完成".encode())

f.close()
s.close()
