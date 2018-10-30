from flask import Flask

# 将当前运行得到主程序构建成Flask的应用，以便接收用户的请求(request),并给出响应(response)
app = Flask(__name__)

#@app.route() Flask中的路由定义，定义用户的访问路径, / 表示的是整个网站的根路径
#def index()，表示匹配上@app.route()路径后的处理程序-视图函数，该类函数必须要有return，return后要给一个字符串 或 响应对象
@app.route('/')
def index():
    return "<h1>this is my first flask app</h1>"

if __name__ == '__main__':
    # 运行Flask应用(启动Flask的服务)，默认在本机开启的端口号是5000,debug=True,是将当前的启动模式改为调试模式(开发环境中推荐使用调试模式,生产环境中不允许使用)
    app.run(debug=True)






