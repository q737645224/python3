from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

import pymysql
from sqlalchemy import or_

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

# 根据现有的表结构构建模型类
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return "<Users %r>" % self.username

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30))
    #反向引用:返回与当前课程相关的teacher列表
    #backref:定义反向关系,本质上会向Teacher实体中增加一个course属性.该属性可替代course_id来访问Course模型.此时获得到的是模型对象,而不是外键值
    teachers=db.relationship('Teacher',backref='course',lazy='dynamic')

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Course %r>" % self.cname

class Teacher(db.Model):
    __tablename__='teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)

    # 增加一列 : course_id,外键列,要引用自主键表(course)的主键列(id)
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))

    #增加反向引用,与 Wife 实体类做一对一引用.允许在Teacher中得到一个Wife的信息.同时,在Wife中也能的到一个Teacher的信息
    # uselist=False , 查询出来的是一个对象,而不是一个列表
    wife = db.relationship('Wife',backref='teacher',uselist=False)

    def __init__(self,tname,tage):
        self.tname = tname
        self.tage = tage

    def __repr__(self):
        return "<Teacher %r>" % self.tname

class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    wage = db.Column(db.Integer)
    #增加一个列:表示引用自teacher表的主键
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))

    def __init__(self,wname,wage):
        self.wage = wage
        self.wname = wname

    def __repr__(self):
        return "<Wife %r>" % self.wname

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30))
    # 增加关联属性以及反向引用
    courses=db.relationship(
        'Course',
        secondary='student_course',
        lazy='dynamic',
        backref = db.backref(
            'students',
            lazy='dynamic'
        )
    )

    def __init__(self,sname):
        self.sname = sname

    def __repr__(self):
        return "<Student %r>" % self.sname

student_course = db.Table(
    'student_course',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
    db.Column('couse_id',db.Integer,db.ForeignKey('course.id'))
)

# db.drop_all()
db.create_all()

@app.route('/insert')
def insert_views():
    user = Users('老魏',40,'laowei@163.com')
    db.session.add(user)
    return "Insert OK"

@app.route('/query')
def query_views():
    # 测试查询
    # print(db.session.query(Users))
    # print(db.session.query(Users.username,Users.email))
    # print(db.session.query(Users,Course))



    #通过查询执行函数获得最终查询结果
    # all() : 得到查询中所有的结果
    # users = db.session.query(Users).all()
    # for u in users:
    #     print(u.username,u.age,u.email)


    #first() : 得到查询中的第一个结果
    # user = db.session.query(Users).first()
    # print(user.username,user.age,user.email)
    # course = db.session.query(Course).first()
    # print(course)




    # 使用查询过滤器函数对数据进行筛选

    # 查询年龄大于30的Users的信息
    # users = db.session.query(Users).filter(Users.age>30).all()
    # print(users)

    #查询年龄大于30并且id大于5的Users的信息
    # users = db.session.query(Users).filter(Users.age>30,Users.id > 5).all()
    # print(users)

    #查询年龄大于30 或者 id大于 5 的Users的信息
    # users = db.session.query(Users).filter(or_(Users.age>30,Users.id > 5)).all()
    # print(users)

    #查询email中包含字符'w'的用户的信息
    # users = db.session.query(Users).filter(Users.email.like('%w%')).all()
    # print(users)

    #查询id在1,2,3 之间的 用户的信息
    # users = db.session.query(Users).filter(Users.id.in_([1,2,3])).all()
    # print(users)

    #查询 Users 表中所有数据的前3条
    # users = db.session.query(Users).limit(3).all()
    # users = db.session.query(Users).limit(3).offset(1).all()

    # 查询Users表中所有的数据,并按照id倒叙排序
    # users = db.session.query(Users).order_by('id desc,age asc')
    # print(users)

    # 查询Users表中所有的数据,并按照 age 进行分组
    # users = db.session.query(Users).group_by('id').all()
    # print(users)



    # 基于Models实现的查询 : 查询id>3的所有用户的信息
    users = Users.query.filter(Users.id>3).all()
    print(users)
    return "Query OK"

@app.route('/query_all')
def query_all():
    # 查询Users表中所有的数据
    users = db.session.query(Users).all()
    # 将查询结果放到模板中进行显示
    return render_template('01-users.html',params=locals())

# @app.route('/query_by_id/<int:id>')
# def query_by_id(id):
#     user = db.session.query(Users).filter_by(id=id).first()
#     return render_template('02-user.html',params=locals())

@app.route('/query_by_id')
def query_by_id():
    # 接收前端通过地址栏传递过来的查询字符串
    id = request.args.get('id')
    # 根据id获取 user 的信息
    user = db.session.query(Users).filter_by(id=id).first()
    # 将user对象发送的02-user.html模板上进行s显示
    return render_template('02-user.html',params=locals())


@app.route('/delete_user')
def delete_user():
    user = Users.query.filter_by(id=5).first()
    db.session.delete(user)
    return 'Delete OK'

@app.route('/update_user')
def update_user():
    user = Users.query.filter_by(id=1).first()
    user.username = "Wang WC"
    user.age = 40
    db.session.add(user)
    return "Update OK"


@app.route('/delete')
def delete_views():
    # 接收请求过来的id值
    id = request.args.get('id')
    # 根据id值查询出对应的模型对象
    user = Users.query.filter_by(id=id).first()
    # 将模型对象删除
    db.session.delete(user)

    url=request.headers.get('referer','/query_all')
    return redirect(url)


@app.route('/update',methods=['GET','POST'])
def update_views():
    if request.method == 'GET':
        # 获取前端传递过来的 id
        id = request.args.get('id')
        # 根据id查询出对应的实体对象
        user = Users.query.filter_by(id=id).first()
        # 将实体对象放到03-update.html模板中显示
        return render_template('03-update.html',params=locals())
    else:
        #接收前端传递过来的四个参数
        id = request.form['id']
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        # 查
        user = Users.query.filter_by(id=id).first()
        # 改
        user.username = username
        user.age = age
        user.email = email
        # 保存
        db.session.add(user)
        return redirect('/query_all')

@app.route('/add_course')
def add_course():
    course1 = Course('PYTHON 基础')
    course2 = Course('PYTHON 高级')
    course3 = Course('PYTHON WEB 基础')
    course4 = Course('PYTHON WEB 开发')

    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    return "Add Course OK"

@app.route('/add_teacher')
def add_teacher():
    teacher = Teacher('魏老师',35)
    # teacher.course_id = 1
    # 根据course_id查询出一个Course实体,再将Course实体赋值给teacher
    # course=Course.query.filter_by(id=1).first()
    course = db.session.query(Course).filter_by(id=1).first()
    # print(course)
    teacher.course = course
    db.session.add(teacher)

    return "Add teacher OK"

@app.route('/register_teacher',methods=['POST','GET'])
def register_teacher():
    if request.method == 'GET':
        courses = Course.query.all()
        return render_template('04-register.html',params = locals())
    else:
        # 获取提交过来的三个数据
        tname = request.form['tname']
        tage = request.form['tage']
        course_id = request.form['course_id']
        # 根据提交过来的course_id查询出对应的course对象
        course = Course.query.filter_by(id=course_id).first()
        # 创建teacher对象并将course对象赋值给teacher对象
        teacher = Teacher(tname,tage)
        teacher.course = course
        #将teacher对象保存进数据库
        db.session.add(teacher)
        return redirect('/show_teacher')

@app.route('/query_teacher')
def query_teacher():
    # 通过 course 查询对应所有的 teacher
    # 查询 id 为1 的course对象
    # course = Course.query.filter_by(id=1).first()
    # 根据course对象查询所有的teacher对象
    # teachers = course.teachers.all()

    # 通过teacher查询course
    teacher = Teacher.query.filter_by(tname='吕老师').first()
    course = teacher.course
    print('老师:%s,课程:%s' % (teacher.tname,course.cname))
    return "Query OK"

@app.route('/show_teacher')
def show_teacher():
    teachers = Teacher.query.all()
    return render_template('05-showteacher.html',params=locals())

@app.route('/query_teacher_course')
def query_teacher_course():
    results = db.session.query(Teacher,Course).filter(Teacher.course_id == Course.id).all()

    for result in results:
        print("姓名:%s,课程:%s" % (result.Teacher.tname,result.Course.cname))
    return "Query OK"

@app.route('/add_wife')
def add_wife():
    # 查询 王老师 的信息
    tea=Teacher.query.filter_by(tname='王老师').first()
    # 创建 wife 对象
    wife=Wife('王夫人',16)
    # 将 王老师 对象 赋值给 wife
    wife.teacher=tea
    # 将 wife 保存回数据库
    db.session.add(wife)
    return "Add wife OK"

@app.route('/query_wife')
def query_wife():
    # 通过 teacher 找 wife
    # teacher= Teacher.query.filter_by(tname='王老师').first()
    # wife = teacher.wife
    # print("%s的媳妇是%s" % (teacher.tname,wife.wname))
    # 通过 wife 找 teacher
    wife=Wife.query.filter_by(wname='王夫人').first()
    teacher=wife.teacher
    print("%s的官人是%s" % (wife.wname,teacher.tname))

    return "Query OK"

@app.route('/register_wife',methods=['GET','POST'])
def register_wife():
    if request.method == 'GET':
        # 查询 Teacher 列表 发送到模板上
        teachers = Teacher.query.all()
        return render_template('06-wife.html',params=locals())
    else:
        # 接收 teacher 的 value
        teacher_id = request.form['teacher']
        # 判断 wife 表中的 teacher_id 列是否已经有了value的值
        wife=Wife.query.filter_by(teacher_id=teacher_id).first()
        if wife:
            errMsg = "EXIST"
            teachers = Teacher.query.all()
            return render_template('06-wife.html',params=locals())
        else:
            # 接收剩余数据
            wname = request.form['wname']
            wage = request.form['wage']
            # 根据teacher_id查询teacher对象
            teacher = Teacher.query.filter_by(id=teacher_id).first()
            # 创建wife对象并保存回数据库
            wife = Wife(wname,wage)
            wife.teacher = teacher
            db.session.add(wife)
            return 'OK'

# 向多对多的关联表中增加数据
@app.route('/add_student_course')
def add_student_course():
    # 查询 张三丰 的信息
    stu = Student.query.filter_by(sname='张三丰').first()
    # 查询 PYTHON基础 的信息
    cour = Course.query.filter_by(id=2).first()
    # 将cour课程追加到stu的courses列表中
    stu.courses.append(cour)
    db.session.add(stu)
    return "Add OK"

@app.route('/query_student_course')
def query_student_course():
    # 查询张三丰所选的所有课程
    student = Student.query.filter_by(id=1).first()
    courses = student.courses.all()
    print('学员姓名:%s' % student.sname)
    for cour in courses:
        print('所选课程:%s' % cour.cname)

    return "Query OK"

if __name__ == "__main__":
    app.run(debug=True)