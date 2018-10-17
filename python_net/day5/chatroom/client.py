from socket import * 
import sys,os 

def login(s,ADDR):
    while True:
        name = input("请输入用户名:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        #接收登录结果
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("@进入聊天室@")
            return name
        else:
            print(data.decode())
#发送消息
def do_child(s,name,addr):
    while True:
        text = input("发言(quit退出):")
        #退出
        if text.strip() == "quit":
            msg = "Q " + name 
            s.sendto(msg.encode(),addr)
            sys.exit("退出聊天室")

        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),addr)

#接收消息
def do_parent(s):
    while True:
        msg,addr = s.recvfrom(1024)
        if msg.decode() == 'EXIT':
            sys.exit(0)
        print(msg.decode()+"\n发言(quit退出):",end="")

#main控制套接字的创建
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket(AF_INET,SOCK_DGRAM)
    
    name = login(s,ADDR)
    if name:
        pid = os.fork()
        if pid < 0:
            sys.exit("创建子进程失败")
        elif pid == 0:
            do_child(s,name,ADDR)
        else:
            do_parent(s)
    else:
        return 


if __name__ == "__main__":
    main()