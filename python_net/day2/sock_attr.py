from socket import * 

s = socket()

#设置端口可立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

#获取套接字类型
print(s.type)
#获取地址类型
print(s.family)

#文件描述符
print(s.fileno())

s.bind(('172.60.50.181',9999))
#获取绑定地址
print(s.getsockname())

s.listen(5)

c,addr = s.accept()

print(c.getpeername())
print("addr:",addr)

data = c.recv(1024)
print(data)

c.close()
s.close()

