# property.py


class Student:
    def __init__(self, s):
        self.__score = s  # 私有属性,不让其它人任意修改成绩

    @property
    def score(self):
        '''取值实现getter方法'''
        print('正在取值')
        return self.__score

    @score.setter
    def score(self, v):
        '''实现设置者setter,对用户的赋值加以限制'''
        assert 0 <= v <= 100, '成绩不合法'
        self.__score = v


s = Student(59)
print(s.score)  # 希望有一个属能得到成绩
s.score = 80  # 通过s.score 来修改成功
print(s.score)  # 80


