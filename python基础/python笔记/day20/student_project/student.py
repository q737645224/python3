# student.py


class Student:
    def __init__(self, n, a, s):
        self.__name, self.__age, self.__score = n, a, s

    def get_info(self):
        '''此方法 为调用者提供姓名,年龄,成绩组成的元组'''
        return (self.__name, self.__age, self.__score)

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def write_to(self, f):
        f.write(self.__name)
        f.write(',')
        f.write(str(self.__age))
        f.write(',')
        f.write(str(self.__score))
        f.write('\n')


