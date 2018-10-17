# 2. 输入一个圆的面积，打印出这个圆的半径

import math as m  # m为math的新名字

area = float(input("请输入圆的面积: "))

t = area / m.pi
r = m.sqrt(t)
print('半径是:', r)
