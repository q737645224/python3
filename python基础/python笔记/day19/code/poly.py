# poly.py


# 此示例示意python中的运行时状态
class Shape:
    def draw(self):
        print('Shape的draw方法被调用')


class Point(Shape):
    def draw(self):
        print("正在画一个点")


class Circle(Shape):
    def draw(self):
        print("正在画一个圆")


def my_draw(s):
    s.draw()  # 此处调用哪儿方法呢? 此处显示出'动态'


s1 = Circle()
s2 = Point()
my_draw(s2)
my_draw(s1)






