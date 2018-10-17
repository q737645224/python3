
# 4 实现带有界面的学生信息管理系统
#   程序启动时先弹出操作菜单:
#     +-------------------------+
#     | 1)  添加学生信息          |
#     | 2)  显示学生信息          |
#     | 3)  删除学生信息          |
#     | 4)  修改学生成绩          |
#     | q)  退出                 |
#     +-------------------------+
#     请选择: 1
#   要求 ：
#       每个选择都要有一个函数来实现



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


def show_menu():
    print('+-------------------------+')
    print('| 1)  添加学生信息        |')
    print('| 2)  显示学生信息        |')
    print('| 3)  删除学生信息        |')
    print('| 4)  修改学生成绩        |')
    print('| q)  退出                |')
    print('+-------------------------+')


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
        elif s == 'q':
            break

main()








