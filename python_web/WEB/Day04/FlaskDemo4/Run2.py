from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
#指定连接字符串
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#指定让SQLAlchemy自动追踪程序的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#指定执行完操作之后自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#为当前的项目创建一个SQLAlchemy的实例
db = SQLAlchemy(app)


# 创建模型类 - Models
# 创建 Users 类,映射到表中叫 users 表
# 创建字段 : id , 主键,自增
# 创建字段 : username , 长度为80的字符串,不允许为空,必须唯一
# 创建字段 : age , 整数,允许为空
# 创建字段 : email,长度为120的字符串,必须唯一
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return '<Users:%r>' % self.username


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)

    def __init__(self,sname,sage):
        self.sname = sname
        self.sage = sage

    def __repr__(self):
        return '<Student %r>' % self.sname

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)

    def __init__(self,tname,tage):
        self.tname = tname
        self.tage = tage

    def __repr__(self):
        return "<Teacher %r>" % self.tname

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30))

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Course %r>" % self.cname



# 将创建好的实体类映射回数据库
# db.drop_all()
db.create_all()


@app.route('/insert')
def insert_views():
    # 创建 Users 对象
    users = Users('王伟超',38,'wangwc@163.com')
    # 将对象通过db.session.add()插入到数据库
    db.session.add(users)
    # 提交插入操作
    db.session.commit()
    return "Insert Success"

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        # 接收前端传递过来的数据
        username = request.form.get('username')
        age = int(request.form.get('age'))
        email = request.form.get('email')
        # 将数据构建成 Users 对象
        users = Users(username,age,email)
        # 通过 db.session.add 将对象保存进数据库
        db.session.add(users)
        # 提交
        # db.session.commit()
        return "Register OK"


if __name__ == "__main__":
    app.run(debug=True)