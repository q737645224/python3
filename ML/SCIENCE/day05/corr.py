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

# 算收益率,临项差
bhp_returns = np.diff(bhp_closing_prices) / \
    bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / \
    vale_closing_prices[:-1]

# 根据统计学定义自己算相关性矩阵
ave_a = np.mean(bhp_returns)
dev_a = bhp_returns - ave_a  # 离差
var_a = np.mean(dev_a * dev_a)  # 方差
std_a = np.sqrt(var_a)  # 标准差

ave_b = np.mean(vale_returns)
dev_b = vale_returns - ave_b  # 离差
var_b = np.mean(dev_b * dev_b)  # 方差
std_b = np.sqrt(var_b)

cov_aa = var_a
cov_ab = np.mean(dev_a * dev_b)  # 协方差
cov_ba = np.mean(dev_b * dev_a)
cov_bb = var_b

# 相关性矩阵的分子部分:
covs = np.array([
    [cov_aa, cov_ab],
    [cov_ba, cov_bb]
])
# 相关性矩阵的分母部分:
stds = np.array([
    [std_a * std_a, std_a * std_b],
    [std_b * std_a, std_b * std_b]
])
corr = covs / stds
print(corr)

# 用numpy的函数来算相关性矩阵
corr = np.corrcoef(bhp_returns, vale_returns)
print(corr)

mp.figure('Returns', facecolor='lightgray')
mp.title('Returns', fontsize=20)
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

# 画出收益率曲线
dates = dates.astype(md.datetime.datetime)
mp.plot(dates[:-1], bhp_returns, c='orangered',
        label='BHP')
mp.plot(dates[:-1], vale_returns, c='dodgerblue',
        label='VALE')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
