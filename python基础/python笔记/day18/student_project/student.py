# student.py


class Student:
    def __init__(self, n, a, s):
        self.name, self.age, self.score = n, a, s

    def get_info(self):
        '''此方法 为调用者提供姓名,年龄,成绩组成的元组'''
        return (self.name, self.age, self.score)

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score

    def write_to(self, f):
        f.write(self.name)
        f.write(',')
        f.write(str(self.age))
        f.write(',')
        f.write(str(self.score))
        f.write('\n')


