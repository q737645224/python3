# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt 		# 处理日期的
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md  # 处理画图中的日期


def dmy2ymd(dmy):  # unicode有几种编码,包括UCS-4,UTF-8等
    # 默认读进来的是UTF-8类型,UTF-8的一个字符是1至4个字节
    # UCS-4每个字符是固定4字节,符合数组同质性的要求
    dmy = str(dmy, encoding='utf-8')  # 把utf-8转成UCS-4
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    # 告诉它怎么分析日期'%d-%m-%Y'
    ymd = date.strftime('%Y-%m-%d')
    return ymd


dates, opening_prices, highest_prices, lowest_prices,\
    closing_prices = np.loadtxt(
        '../data/aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        converters={1: dmy2ymd},
        # 先用dmy2ymd函数转换日期,返回值再转成dtype里的M8[D]
        dtype=np.dtype('M8[D], f8, f8, f8, f8')
        # numpy只能处理年月日,所以需要converters先做转换
    )

mp.figure('K-Day', facecolor='lightgray')
mp.title('K-Day', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))  # 主刻度画在周一上
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%d %b %Y'))  # 主刻度标签日期格式化器
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 把numpy里的M8[D]类型转成md.datetime.datetime类型:
dates = dates.astype(md.datetime.datetime)

# 得到布尔数组:
rise = closing_prices - opening_prices >= 0.01
fall = opening_prices - closing_prices >= 0.01

# 初始化一个全零数组,元素个数和交易日一样多
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
# 把一个布尔数组放到另一个数组的下标,作为掩码
fc[rise], fc[fall] = (1, 1, 1), (0, 0.5, 0)
ec[rise], ec[fall] = (1, 0, 0), (0, 0.5, 0)

mp.bar(dates, highest_prices - lowest_prices, 0,
       lowest_prices, color=fc, edgecolor=ec)
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=fc, edgecolor=ec)

mp.gcf().autofmt_xdate()  # 自动格式化x轴上的日期
mp.show()
