#student_info.py
def input_student(l):
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        try:
            age = int(input("请输入年龄："))
            while not age :
                age =int(input("请输入年龄："))
            score = int(input("请输入成绩："))
            while not score :
                score = int(input("请输入成绩："))
        except:
            continue
        d = {}
        d["name"] = name
        d["age"] = age
        d["score"] = score
        l.append(d)
    return l

def output_student(l):
    print("+" + "-"* 12 + \
        "+" + "-" * 10 + \
        "+" + "-" * 9 + "+")
    print("|", "name".center(10), \
        "|", "age".center(8), "|", \
        "score".center(6), "|" )
    print("+" + "-"* 12 + "+" +\
     "-" * 10 + "+" + "-" * 9 + "+")
    for i in l:
        n = i["name"]
        a = i["age"]
        s = i["score"]
        print("|", \
            n.center(10), "|",\
            str(a).center(8), "|", \
            str(s).center(6), "|" )
        #print("|"%s"|"%s"|"%s"|")
    print("+" + "-"* 12 + \
        "+" + "-" * 10 + \
        "+" + "-" * 9 + "+")

def Pop_student(valus,l):
    for i in l:
        n = i["name"]
        if valus == n:
            l.remove(i)

def repair_student(valus, l):  #修改学生信息
    for i in l:             #遍历Ｌ
        n = i["name"]
        if valus == n:
            print("输入修改的信息：\n")
            name = input("请输入姓名：")
            age = input("请输入年龄：")
            score = input("请输入成绩：")
            i["name"] = name
            i["age"] = age
            i["score"] = score
            print("修改成功")
            break
    else:
        print("你输入的姓名不在！")


def sorted_gradel(l):
    def grades(i):
        return i["score"]  #返回关键字为成绩的值
    list_ = sorted(l,key=grades)
    output_student(list_)

def sorted_gradeh(l):
    def grades(i):
        return i["score"]
    list_ = sorted(l,key=grades, reverse=True)
    output_student(list_)

def sorted_ageh(a):
    def ages(i):
        return i["age"]  #返回关键字为年龄的值
    age_ =sorted(a,key = ages, reverse = True)
    output_student(age_)

def sorted_agel(a):
    def ages(i):
        return i["age"]
    age_ =sorted(a,key = ages)
    output_student(age_)

def read_info(l):
    try:
        f = open("si.txt", "rb")
        try:
            rl = []
            while True:
                L = f.readline()
                if L == "":
                    break
                name, age, score = L.split
                age = int(age) #转为整数
                score = int(score)
                rl.append({'name':name,
                                'age':age,
                                'score': score})
            return rl  #返回列表
        finally:
            f.close()
    except OSError:
        print("打开文件失败")

def write_info(l):
    f = open("si.txt", 'w')
    for i in l:
        f.write(i["name"]," ")
        f.write(str(i["age"]))
        f.write(str(i["score"]))
        f.write("\n")
    f.close()



