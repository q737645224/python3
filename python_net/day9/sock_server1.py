from socketserver import * 

#创建服务器类
class Server(ThreadingMixIn,UDPServer):
    pass 

class Handler(DatagramRequestHandler):
    def handle(self):
        while True: 
            data = self.rfile.readline()
            print(self.client_address)
            if not data:
                break 
            print(data.decode())
            self.wfile.write(b"Receive")

if __name__ == "__main__":
    server_addr = ('0.0.0.0',8888)

    #创建服务器对象
    server = Server(server_addr,Handler)
    #启动服务器
    server.serve_forever()