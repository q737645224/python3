from socket import * 
import os,sys

#发送管理员消息
def do_child(s,addr):
    while True:
        msg = input("管理员消息:")
        msg = "C 管理员 " + msg 
        s.sendto(msg.encode(),addr)
    
#用户登录
def do_login(s,user,name,addr):
    if (name in user) or name == "管理员":
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr)
    #通知所有人
    msg = "\n欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #插入user
    user[name] = addr 

def do_chat(s,user,name,data):
    msg = "\n{} 说: {}".format(name,data)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,user,name):
    msg = "\n%s 离开了聊天室"%name 
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name] #删除离开的用户


#接收客户端请求并处理
def do_parent(s):
    # 用于存储用户 {'Alex':('127.0.0.1',8888)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        if msgList[0] == 'L':
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == 'C':
            # "C Levi [I miss you]"
            data = ' '.join(msgList[2:])
            do_chat(s,user,msgList[1],data)
        elif msgList[0] == 'Q':
            do_quit(s,user,msgList[1])    


# 创建套接字，网络连接，创建父子进程
def main():
    #server address
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    elif pid == 0:
        do_child(s,ADDR)
    else:
        do_parent(s)

if __name__ == "__main__":
    main() 

