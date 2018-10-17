from socketserver import * 

#创建服务器类
# class Server(ForkingMixIn,TCPServer):
# class Server(ForkingTCPServer):
class Server(ThreadingMixIn,TCPServer):
    pass 

class Handler(StreamRequestHandler):
    def handle(self):
        #self.request ==> accept 返回的套接字
        print("Connect from",\
            self.request.getpeername()) 
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'Receive')


if __name__ == "__main__":
    server_addr = ('0.0.0.0',8888)

    #创建服务器对象
    server = Server(server_addr,Handler)
    #启动服务器
    server.serve_forever()