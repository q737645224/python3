# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
ax = mp.gca()
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

plot = mp.plot([], [], c='orangered')[0]

plot.set_data([], [])  # 将容器类型设置成列表类型


def update(data):  # 传入的参数是生成器传来的数据
    t, v = data
    x, y = plot.get_data()  # 用x,y拿到曲线x,y坐标的两个列表容器
    x.append(t)
    y.append(v)
    plot.set_data(x, y)  # 把x,y传回给图形对象
    # 如果图线触及到屏幕右端,则延长x轴
    x_min, x_max = ax.get_xlim()
    if t >= x_max:
        ax.set_xlim(x_min, x_max * 2)
        ax.figure.canvas.draw()  # 重新绘制
        #ax.set_xlim(x_max, x_max * 2)


def generator():  # 生成器函数
    t = 0
    for i in range(10000):
        v = np.sin(2 * np.pi * t) * np.exp(-t / 8)
        yield t, v  # 执行到yield时,函数会返回一个迭代值
        # 下次迭代时代码会从yield下面继续执行
        t += 0.05

anim = ma.FuncAnimation(mp.gcf(), update,
                        generator, interval=5)
mp.show()
