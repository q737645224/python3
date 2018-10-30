# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np


def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy,
                                '%d-%m-%Y').date()
    wday = date.weekday()
    return wday

wdays, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        '../data/aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        converters={1: dmy2wday})

# 统计前三周(工作日)的信息
wdays = wdays[:19]
opening_prices = opening_prices[:19]
highest_prices = highest_prices[:19]
lowest_prices = lowest_prices[:19]
closing_prices = closing_prices[:19]

# 取出第一个星期一的下标
first_monday = np.where(wdays == 0)[0][0]
print(np.where(wdays == 0))
# 取出最后一个星期五的下标
last_friday = np.where(wdays == 4)[0][-1]
indices = np.arange(first_monday, last_friday + 1)
indices = np.split(indices, 3)  # 等分成3段,3个每周下标
print(indices)


def week_summary(indice):  # 参数indice是一周的下标值
    # 周一的开盘价:
    opening_price = opening_prices[indice[0]]
# 这周的最高价格:
    highest_price = np.max(np.take(
        highest_prices, indice))
# 这周的最低价格:
    lowest_price = np.min(np.take(
        lowest_prices, indice))
# 本周最后一天的收盘价:
    closing_price = closing_prices[indice[-1]]
    return opening_price, highest_price,\
        lowest_price, closing_price

summaries = np.apply_along_axis(week_summary, 1,
                                indices)
print(summaries)

# 保存文件:
np.savetxt('../data/summary_new.csv', summaries,
           delimiter=',', fmt='%g')
# fmt='%g'为紧凑浮点型
