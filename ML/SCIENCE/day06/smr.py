# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
warnings.filterwarnings('ignore',
                        category=np.RankWarning)


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy,
                                '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd

dates, bhp_closing_prices = np.loadtxt(
    '../data/bhp.csv',
    delimiter=',', usecols=(1, 6),
    unpack=True, dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd}
)
dates, vale_closing_prices = np.loadtxt(
    '../data/vale.csv',
    delimiter=',', usecols=(1, 6),
    unpack=True, dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd}
)

# 计算回报率:
bhp_returns = np.diff(bhp_closing_prices) / \
    bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / \
    vale_closing_prices[:-1]

# 去除噪声后,趋势线的交汇点才是真的交汇点
N = 8  # 卷积核宽度取8
weights = np.hanning(N)  # 宽度为8个元素的汗宁窗
weights /= weights.sum()  # 卷积核

# 去除噪声
bhp_smooth_returns = np.convolve(
    bhp_returns, weights, 'valid')
vale_smooth_returns = np.convolve(
    vale_returns, weights, 'valid')

# 用多项式拟合两条曲线,得到多项式的x,y和系数p
days = dates[N - 1:-1].astype(int)
degree = 5  # 用来设多项式的最高次幂

# 求方程系数p
bhp_p = np.polyfit(days, bhp_smooth_returns, degree)

# 推出拟合的y值:
bhp_poly_returns = np.polyval(bhp_p, days)

vale_p = np.polyfit(days, vale_smooth_returns, degree)
vale_poly_returns = np.polyval(vale_p, days)

# 求多项式系数p3:
sub_p = np.polysub(bhp_p, vale_p)

roots = np.roots(sub_p)
reals = roots[np.isreal(roots)].real

inters = []  # 用来装交点坐标
for real in reals:
    if days[0] <= real and real <= days[-1]:
        inters.append([real, np.polyval(bhp_p, real)])
inters.sort()
inters = np.array(inters)

mp.figure('Smoothing Returns', facecolor='lightgray')
mp.title('Smoothing Returns', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Returns', fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
    md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

dates = dates.astype(md.datetime.datetime)
# 画图,平滑处理之前:
mp.plot(dates[:-1], bhp_returns, c='orangered',
        alpha=0.25, label='BHP')
mp.plot(dates[:-1], vale_returns, c='dodgerblue',
        alpha=0.25, label='VALE')

# 画用卷积做平滑处理后的走势:
mp.plot(dates[N - 1:-1], bhp_smooth_returns,
        c='orangered', alpha=0.75, label='BHP')
mp.plot(dates[N - 1:-1], vale_smooth_returns,
        c='dodgerblue', alpha=0.75, label='VALE')

# 画多项式拟合出来的走势:
mp.plot(dates[N - 1:-1], bhp_poly_returns,
        c='orangered', linewidth=3, label='BHP')
mp.plot(dates[N - 1:-1], vale_poly_returns,
        c='dodgerblue', linewidth=3, label='VALE')

# 把inters数组水平分割,得到日期和回报:
dates, returns = np.hsplit(inters, 2)

dates = dates.astype(int).astype('M8[D]').astype(
    md.datetime.datetime)
mp.scatter(dates, returns, marker='x',
           c='firebrick', s=120, lw=3, zorder=3)

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
