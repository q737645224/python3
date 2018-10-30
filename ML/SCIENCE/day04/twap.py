# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np


def dmy2days(dmy):
    dmy = str(dmy, encoding='utf-8')  # UTF-8->UCS-4
    date = dt.datetime.strptime(dmy,
                                '%d-%m-%Y').date()
    days = (date - dt.date.min).days
    # dt.date.min即时间原点
    return days

days, closing_prices = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',',
    usecols=(1, 6),
    unpack=True,
    converters={1: dmy2days}
)

twap, sw = 0, 0
for closing_price, day in zip(closing_prices,
                              days):
    twap += closing_price * day
    sw += day
twap /= sw
print(twap)

twap = closing_prices.dot(days) / days.sum()
print(twap)

twap = np.average(closing_prices, weights=days)
print(twap)
