
# 导入学生Student类
from student import Student


def input_student():
    L = []  # 创建一个容器准备放入
    while True:
        name = input('请输入姓名: ')
        if not name:  # 如果名字为空,结束输入操作
            break
        age = int(input("请输入年龄: "))
        score = int(input("请输入成绩: "))
        d = Student(name, age, score)
        L.append(d)
    return L


def output_student(lst):
    # 打印表格
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in lst:
        name, age, score = d.get_info()
        n = name.center(15)
        a = str(age).center(10)
        s = str(score).center(10)
        print("|%s|%s|%s|" % (n, a, s))

    print("+---------------+----------+----------+")


def output_student_by_score_desc(lst):
    def k(d):
        return d.get_score()
    L = sorted(lst, key=k, reverse=True)
    output_student(L)


def output_student_by_score_asc(lst):
    L = sorted(lst, key=lambda d: d.get_score())
    output_student(L)


def output_student_by_age_desc(lst):
    L = sorted(lst, key=lambda d: d.get_age(),
               reverse=True)
    output_student(L)


def output_student_by_age_asc(lst):
    L = sorted(lst, key=lambda d: d.get_age())
    output_student(L)


def save_to_file(lst, filename='si.txt'):
    try:
        f = open(filename, 'w')
        for s in lst:
            s.write_to(f)
        f.close()
    except OSError:
        print("保存文件失败")
    else:
        print("保存文件成功")


def read_from_file(filename='si.txt'):
    L = []
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()  # 去掉 '\n'
                n, a, s = line.split(',')  # 拆为三个元素
                a = int(a)  # 转为整数
                s = int(s)
                L.append(Student(n, a, s))
    except OSError:
        print("读取文件失败")
    return L


