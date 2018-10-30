# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy,
                                '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd

dates, closing_prices = np.loadtxt(
    '../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd}
)

N = 3
pred_prices = np.zeros(
    closing_prices.size - 2 * N + 1)  # 前2N天的价格用来解方程组
for i in range(pred_prices.size):
    a = np.zeros((N, N))  # 初始化a矩阵,N*N
    for j in range(N):  # 用j表示a的行号
        a[j] = closing_prices[i + j:i + j + N]
        # 每次循环生成a的一行数据,最终生成a矩阵
    b = closing_prices[i + N:i + N * 2]  # b向量
    x, residuals, rank, s = np.linalg.lstsq(a, b)
    # 向量x,残差,置信度,标准差
    pred_prices[i] = b.dot(x)  # 点乘,求出预测值
    print(a.dot(x), b, pred_prices[i])

mp.figure('Stock Price Prediction',
          facecolor='lightgray')
mp.title('Stock Price Prediction', fontsize=20)
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

dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, 'o-',
        c='lightgray', label='Closing Price')

# 在dates数组的最后添加上多预测的一天:
dates = np.append(
    dates, dates[-1] + pd.tseries.offsets.BDay())
# 预测的这天无法确认是否越过周末,
# 所以利用pandas里的BDay(),(BDay=Bussiness Day)
# tseries时间序列,offsets计算时间增量

# 画预测的价格
mp.plot(dates[2 * N:], pred_prices, 'o',
        c='orangered', label='Predicted Price')
# 因为前2N天的价格用来计算预测值,所以切片掉前2N

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
