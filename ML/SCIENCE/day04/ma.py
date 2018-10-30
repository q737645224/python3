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

dates, closing_prices = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',',
    usecols=(1, 6),
    unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})

sma5a = np.zeros(closing_prices.size - 4)
# 5日均线开头会少4个点,所以减4

# 用传统算法计算:
for i in range(sma5a.size):
    sma5a[i] = closing_prices[i:i + 5].mean()

# 用卷积函数计算:
sma5b = np.convolve(closing_prices, np.ones(5) / 5,
                    'valid')  # 卷积核是5个1/5
sma10 = np.convolve(closing_prices, np.ones(10) / 10,
                    'valid')  # 卷积核是10个1/10

# 产生一个按指数规律变化的权重,越往后权重越大
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights[::-1],
                   'valid')

mp.figure('Moving Average', facecolor='lightgray')
mp.title('Moving Average', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))

mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 画出几条均线做对比:
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, c='dodgerblue',
        label='Closing Price')
mp.plot(dates[4:], sma5a, c='orangered',
        label='SMA-5A')
mp.plot(dates[4:], sma5b, c='orangered',
        alpha=0.25, linewidth=6, label='SMA-5B',
        zorder=1)
mp.plot(dates[9:], sma10, c='limegreen',
        label='SMA-10')
mp.plot(dates[4:], ema5, c='red', label='EMA-5A')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
