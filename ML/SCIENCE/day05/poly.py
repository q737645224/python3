# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
warnings.filterwarnings('ignore',
                        category=np.RankWarning)  # 忽略一些警告


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

mp.figure('Polynomial Fitting', facecolor='lightgray')
mp.title('Polynomial Fitting', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
    md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 分析两支股票的价格之差
diff_closing_prices = bhp_closing_prices - \
    vale_closing_prices

# 用多项式拟合函数进行计算:
# 把日期转换成整数:
days = dates.astype(int)
# 用polyfit求泰勒展开里的p, 5阶
p = np.polyfit(days, diff_closing_prices, 5)
# 把系数p,横坐标days代入,算出拟合的纵坐标的值
poly_closing_prices = np.polyval(p, days)

dates = dates.astype(md.datetime.datetime)
# 画多项式拟合出的曲线:
mp.plot(dates, poly_closing_prices, c='dodgerblue',
        linewidth=3, label='Polynomial Fitting')

# 差价的散点图:
mp.scatter(dates, diff_closing_prices, c='limegreen',
           alpha=0.5, s=80, label='Difference Price')

# 切线斜率为0(也就是导函数为0)的点,为拐点
q = np.polyder(p)  # 得到一阶微分方程的系数数组q
roots = np.roots(q)  # 求根,负根,虚根不要
reals = roots[np.isreal(roots)].real
# np.isreal()返回的是一个布尔型数组,True对应的就是实根
#.real用来去掉实根虚部的0j

# 峰值数组,装第一个点,最后一个点,以及拐点
# 加入第一个点:
peeks = [[days[0], np.polyval(p, days[0])]]

for real in reals:
    # 在第一天和最后一天区间内的reals(拐点)值才保留
    if days[0] <= real and real <= days[-1]:
        peeks.append([real, np.polyval(p, real)])
# 加入最后一个点:
peeks.append([days[-1], np.polyval(p, days[-1])])

peeks.sort()
peeks = np.array(peeks)  # 把peeks变成数组

# 将peeks拆成日期和价格两个一维数组:
dates, prices = np.hsplit(peeks, 2)

dates = dates.astype(int).astype('M8[D]').astype(
    md.datetime.datetime)  # 方程的解是浮点型

# 用箭头连接这几个拐点:
for i in range(1, dates.size):
    mp.annotate('', xytext=(dates[i - 1],
                            prices[i - 1]),
                xy=(dates[i], prices[i]), size=40,
                arrowprops=dict(arrowstyle='fancy',
                                color='orangered',
                                alpha=0.25))
# 用红三角标注峰值点:
mp.scatter(dates, prices, marker='^', c='orangered',
           s=100, label='Peek', zorder=4)

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
