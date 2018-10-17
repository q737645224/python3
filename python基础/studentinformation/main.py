#main.py
from menu import show_menu
from student_info import *

def main():
    L = []
    show_menu()
    while True:
        i = input("请选择：")
        if i == "q":
            break
        elif i == "1":
            input_student(L)
        elif i == "2":
            output_student(L) 
        elif i == "3":
            name = input("删信息人的姓名：")
            Pop_student(name, L)
        elif i == "4":
            name = input("请输入要修改人的姓名：")
            repair_student(name, l)
        elif i == "5":
            print("修改后的列表为：")
            sorted_gradeh(L)   
        elif i == "6":
            print("修改后的列表为：")
            sorted_gradel(L)
        elif i == "7":
            print("修改后的列表为：")
            sorted_ageh(L)
        elif i == "8":
            print("修改后的列表为：")
            sorted_agel(L)
        elif i == "9":
            write_info(L)
        elif i == "10":
            L = read_info()


if __name__ == "__main__" :
    main()
