
# 3. 改写之前的学生信息管理程序
# 　　要求添加四个功能:
#     | 5) 按学生成绩高-低显示学生信息　|
#     | 6) 按学生成绩低-高显示学生信息　|
#     | 7) 按学生年龄高-低显示学生信息　|
#     | 8) 按学生年龄低-高显示学生信息　|



def input_student():
    L = []  # 创建一个容器准备放入
    while True:
        name = input('请输入姓名: ')
        if not name:  # 如果名字为空,结束输入操作
            break
        age = int(input("请输入年龄: "))
        score = int(input("请输入成绩: "))
        d = {}  # 每次都会执行{} 来创建新的字典
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L


def output_student(lst):
    # 打印表格
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in lst:
        n = d['name'].center(15)
        a = str(d['age']).center(10)
        s = str(d['score']).center(10)
        print("|%s|%s|%s|" % (n, a, s))

    print("+---------------+----------+----------+")


def output_student_by_score_desc(lst):
    def k(d):
        return d['score']
    L = sorted(lst, key=k, reverse=True)
    output_student(L)


def output_student_by_score_asc(lst):
    L = sorted(lst, key=lambda d: d['score'])
    output_student(L)


def output_student_by_age_desc(lst):
    L = sorted(lst, key=lambda d: d['age'],
               reverse=True)
    output_student(L)


def output_student_by_age_asc(lst):
    L = sorted(lst, key=lambda d: d['age'])
    output_student(L)



def show_menu():
    print('+----------------------------------+')
    print('| 1)  添加学生信息                 |')
    print('| 2)  显示学生信息                 |')
    print('| 3)  删除学生信息                 |')
    print('| 4)  修改学生成绩                 |')
    print('| 5)  按学生成绩高-低显示学生信息　|')
    print('| 6)  按学生成绩低-高显示学生信息　|')
    print('| 7)  按学生年龄高-低显示学生信息　|')
    print('| 8)  按学生年龄低-高显示学生信息　|')
    print('| q)  退出                         |')
    print('+----------------------------------+')


def main():
    docs = []  # 用于存放学生信息的空列表
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':
            print("开始删除")
        elif s == '4':
            print("开始修改成绩")
        elif s == '5':
            output_student_by_score_desc(docs)
        elif s == '6':
            output_student_by_score_asc(docs)
        elif s == '7':
            output_student_by_age_desc(docs)
        elif s == '8':
            output_student_by_age_asc(docs)
        elif s == 'q':
            break

main()








