# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
# 将x和y做成1000*1000的点阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 等高线的函数
z = (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)

ax = mp.gca(projection='3d')  # 返回的对象就是导入的axes3d类型对象
mp.title('3D WireFrame', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
ax.plot_wireframe(x, y, z, rstride=10, cstride=10,
                  color='dodgerblue', linewidth=0.5)
mp.show()
