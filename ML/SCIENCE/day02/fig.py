# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

# 生成曲线上各点的x,y坐标,然后用直线连接起来
x = np.linspace(-np.pi, np.pi, 200)  # 产生一个等差数列

# 根据曲线函数计算各点的y坐标
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

# 创建图形对象
mp.figure('Figure Object 1', figsize=(4, 3), dpi=120,
          facecolor='lightgray')
# figsize窗口大小,dpi分辨率

# 设置标题
mp.title('Figure Object 1', fontsize=14)

# 设置坐标轴标签
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
# 前面调用过mp.figure之后,如果没有再次调用,
# 那么之后的操作都是针对当前图形对象的

# 设置刻度标签参数大小
mp.tick_params(labelsize=8)

# 设置网格线
mp.grid(linestyle=':')

# 创建图形对象
mp.figure('Figure Object 2', figsize=(4, 3), dpi=120,
          facecolor='lightgray')
# figsize窗口大小,dpi分辨率

# 设置标题
mp.title('Figure Object 2', fontsize=14)

# 设置坐标轴标签
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
# 前面调用过mp.figure之后,如果没有再次调用,
# 那么之后的操作都是针对当前图形对象的

# 设置刻度标签参数大小
mp.tick_params(labelsize=8)

# 设置网格线
mp.grid(linestyle=':')


# 将由图形名所指定的图形对象设置为当前图形对象,然后画图
mp.figure('Figure Object 1')  # 获取图形对象
mp.plot(x, cos_y, color='orangered',
        label=r'$y=\frac{1}{2}cos(x)$')
mp.legend()

mp.figure('Figure Object 2')  # 获取图形对象
mp.plot(x, sin_y, color='dodgerblue',
        label=r'$y=sin(x)$')
mp.legend()

mp.show()
