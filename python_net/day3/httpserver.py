from socket import * 

# 接收请求
# 查看请求
# 返回客户端段请求内容
def handleClient(connfd):
    request = connfd.recv(4096)
    # print("***********")
    # print(request)
    # print("************")
    #按照行切割请求
    request_lines = request.splitlines()
    for line in request_lines:
        print(line.decode())

    try:
        f = open('index.html')
    except IOError:
        response = "HTTP/1.1 303 Not Found\r\n"
        response += "\r\n"  #空行
        response += '''
                **************************
                Sorry, not found the page.
                **************************
                '''
    else:
        response = "HTTP/1.1 200  OK\r\n"
        response += '\r\n'
        response += f.read()
    finally:
        #发送给浏览器
        connfd.send(response.encode())



#创建套接字，调用handleClient完成功能
def main():
    #创建tcp套接字
    sockfd = socket()
    sockfd.setsockopt\
    (SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen()
    while True:
        print("Listen the port 8000...")
        connfd,addr = sockfd.accept()
        #处理浏览器发来的请求
        handleClient(connfd)
        connfd.close()


if __name__ == "__main__":
    main()
