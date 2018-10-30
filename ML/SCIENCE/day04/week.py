# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np


def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy,
                                '%d-%m-%Y').date()
    wday = date.weekday()  # 用0到6表示星期一到星期日
    return wday

wdays, closing_prices = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',',
    usecols=(1, 6),
    unpack=True,
    converters={1: dmy2wday}
)

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
        # range(5)-> wday=0到4,对应周一到周五
    '''
    ave_closing_prices[wday] = \
        closing_prices[wdays == wday].mean()
    直接用布尔值做掩码
    '''
    '''
    ave_closing_prices[wday] = \
        closing_prices[np.where(wdays == wday)].mean()
    用np.where得到满足条件的下标数组
    '''
    ave_closing_prices[wday] = \
        np.take(closing_prices,
                np.where(wdays == wday)).mean()
    # 用np.take按照np.where中的条件匹配数组元素

print(np.round(ave_closing_prices, 2))
