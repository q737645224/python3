from flask import Flask, render_template

app = Flask(__name__)

class Person(object):

    name = None

    def say(self):
        return "hello i'm a person "

@app.route('/temp')
def temp():
    # dic = {
    #     'title':'我的第一个模板',
    #     'bookName':'钢铁是咋练成的',
    #     'author':'奥斯特洛夫斯基',
    #     'price':32.5,
    #     'publisher':'北京大学出版社',
    # }

    title = '我的第一个模板'
    bookName = '钢铁是咋练成的'
    author = '奥斯特洛夫斯基'
    price = 32.5
    publisher = '北京大学出版社'
    list = ["金毛狮王","青衣父王","紫衫龙王","白眉鹰王"]
    tup = ("刘德华","张学友","黎明","郭富城")
    dic = {
        'LW':'老魏',
        'WWC':'隔壁老王',
        'LZ':'吕泽',
        'MM':'萌萌',
        'PY':'皮爷',
    }
    per = Person()
    per.name = '漩涡鸣人'
    uname = 'uzumaki naruto'

    print(locals())
    return render_template('01_temp.html',params=locals())

@app.route('/login')
def login():
    return '这里是登录页面'

@app.route('/index')
def index():
    return render_template('03-index.html',uname='测试变量')

@app.route('/parent')
def parent():
    return render_template('04-parent.html')

@app.route('/child')
def child():
    return render_template('05-child.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=True)