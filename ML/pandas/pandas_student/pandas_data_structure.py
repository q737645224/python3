import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
s1=pd.Series([90,86,70],index=['leo','kate','john'])
# dict={'leo':90,'kate':86,'john':70}
# s1=pd.Series(dict)
# print(s1[s1>80])
# 2.numpy中的ndarray：
s2=pd.Series(np.random.randn(5),index=list('ABCDE'))
# print(s2)
# 3.数字创建
s3=pd.Series(6)
# print(s3)
# 4.创建一组DataFrame数据-date_range创建时间
date=pd.date_range('20100101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=date,
                columns=list('abcd'))
print(df)
# 对a列数据查找
# print(df.a)
# print(df['a'])
# 对a,b两列数据
# print(df[['a','b']])
# 打印前2行数据
# print(df.head(2))
# print(df[0:2])
df1=df.loc[df.index < '2010-01-04']
print(df1)
df2=df.iloc[:4,[0,1]]
# print(df2)
df3=df.ix[:4,['a','b']]
# print(df3)
# 打印值
print(df.index)