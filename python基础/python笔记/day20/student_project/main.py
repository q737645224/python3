
from menu import show_menu
from student_info import *


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
        elif s == '9':
            save_to_file(docs)  # 保存到文件中
        elif s == '10':
            docs = read_from_file()  # 从文件中读取数据
        elif s == 'q':
            break


if __name__ == '__main__':
    main()
