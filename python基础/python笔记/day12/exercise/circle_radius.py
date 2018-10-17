# 2. 输入一个圆的面积，打印出这个圆的半径 

import math

area = float(input("请输入圆的面积: "))

t = area / math.pi
r = math.sqrt(t)
print('半径是:', r)

