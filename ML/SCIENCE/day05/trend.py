# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy,
                                '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd

dates, opening_prices, highest_prices,\
    lowest_prices, closing_prices = np.loadtxt(
        '../data/aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype=np.dtype('M8[D], f8,f8,f8,f8'),
        converters={1: dmy2ymd}
    )

# 3个价格求平均得到趋势点,也就是方程组的b向量
trend_points = (highest_prices + lowest_prices +
                closing_prices) / 3
# 每天波动的范围:
spreads = highest_prices - lowest_prices
# 压力点:
resistance_points = trend_points + spreads
# 支撑点:
support_points = trend_points - spreads
# 把日期转成一个整数,好参与方程计算:
days = dates.astype(int)

# 做出a向量
a = np.column_stack((days, np.ones_like(days)))

# 根据a,b向量,求趋势线的x向量(k,b)
x = np.linalg.lstsq(a, trend_points)[0]
# 算出趋势线:
trend_line = days * x[0] + x[1]

# 根据压力点,求压力线的函数:
x = np.linalg.lstsq(a, resistance_points)[0]
resistance_line = days * x[0] + x[1]

# 根据支撑点,求支撑线的函数:
x = np.linalg.lstsq(a, support_points)[0]
support_line = days * x[0] + x[1]

mp.figure('Trend', facecolor='lightgray')
mp.title('Trend', fontsize=20)
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

dates = dates.astype(md.datetime.datetime)
rise = closing_prices - opening_prices >= 0.01
fall = opening_prices - closing_prices >= 0.01
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[rise], fc[fall] = (1, 1, 1), (0.85, 0.85, 0.85)
ec[rise], ec[fall] = (0.85, 0.85, 0.85), (0.85, 0.85, 0.85)

# 画k线图
mp.bar(dates, highest_prices - lowest_prices, 0,
       lowest_prices, color=fc, edgecolor=ec)
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=fc, edgecolor=ec)

# 画趋势点和趋势线
mp.scatter(dates, trend_points, c='dodgerblue',
           alpha=0.5, s=80, zorder=2)
mp.plot(dates, trend_line, c='dodgerblue',
        linewidth=3, label='Trend')

# 画压力线和支撑线
mp.scatter(dates, resistance_points, c='orangered',
           alpha=0.5, s=80, zorder=2)
mp.scatter(dates, support_points, c='limegreen',
           alpha=0.5, s=80, zorder=2)
mp.plot(dates, resistance_line, c='orangered',
        linewidth=3, label='Resistance')
mp.plot(dates, support_line, c='limegreen',
        linewidth=3, label='Support')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
