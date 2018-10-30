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
        '../data/bhp.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype=np.dtype('M8[D], f8,f8,f8,f8'),
        converters={1: dmy2ymd}
    )

# 写一个计算收益的函数,开盘价的0.9985倍就买入


def profit(opening_price, highest_price,
           lowest_price, closing_price):
        # 买入价策略:
    buying_price = opening_price * 0.9985
    if lowest_price <= buying_price <= highest_price:
        return (closing_price - buying_price) * 100 / \
            buying_price
    return np.nan  # nan表示无效值

# 将上面定义的标量函数转成矢量函数,并代入参数:
profits = np.vectorize(profit)(
    opening_prices, highest_prices,
    lowest_prices, closing_prices)

# 获得nan位置的布尔数组,nan的位置为True,否则为False:
nan = np.isnan(profits)

# 非nan的值,用~nan按位取反,得到有效值的掩码
dates, profits = dates[~nan], profits[~nan]

# 把收益的和亏损的分开,利用布尔数组做掩码:
gain_dates, gain_profits = \
    dates[profits > 0], profits[profits > 0]
loss_dates, loss_profits = \
    dates[profits < 0], profits[profits < 0]

mp.figure('Trading Simulation', facecolor='lightgray')
mp.title('Trading Simulation', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Profit', fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
    md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

if dates.size > 0:  # dates里至少有一个数据才需要画图
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, profits, c='gray', label='Profit')
    # 在平均值位置上画一条平行于x轴的水平线
    mp.axhline(y=profits.mean(), linestyle=':',
               color='gray')

if gain_dates.size > 0:  # gain_dates里至少有一个数据才需要画图
    gain_dates = gain_dates.astype(md.datetime.datetime)
    mp.plot(gain_dates, gain_profits, 'o',
            c='orangered',
            label='Gain Profit')
    # 在平均值位置上画一条平行于x轴的水平线
    mp.axhline(y=gain_profits.mean(), linestyle=':',
               color='orangered')

if loss_dates.size > 0:  # loss_dates里至少有一个数据才需要画图
    loss_dates = loss_dates.astype(md.datetime.datetime)
    mp.plot(loss_dates, loss_profits, 'o',
            c='limegreen',
            label='Loss Profit')
    # 在平均值位置上画一条平行于x轴的水平线
    mp.axhline(y=loss_profits.mean(), linestyle=':',
               color='limegreen')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
