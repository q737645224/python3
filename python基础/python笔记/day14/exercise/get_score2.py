# 练习:
#   写一个函数 get_score() 来获取学生成绩,
#     要求用户输入 1~100的整数,输果输入出现异常,返此函数返回0,
#     否则返回用户输入的成绩
#   示例:
#     def get_score():
#         ...
#     score = get_score()
#     print("学生的成绩是:", score)


def get_score():
    s = int(input("请输入成绩(0~100): "))
    if not (0 <= s <= 100):
        return 0
    return s


try:
    score = get_score()
except:
    score = 0
print("学生的成绩是:", score)
