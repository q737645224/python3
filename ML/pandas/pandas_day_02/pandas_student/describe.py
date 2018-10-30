import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(50).reshape(10,5),columns=list('abcde'))
# print(df)
# print(df.describe())
# print(df.sem())

ss = pd.Series(['Tokyo', 'Nagoya', 'Nagoya', 'Osaka', 'Tokyo', 'Tokyo'])
# 东京 名古屋 大阪
# print(ss.value_counts())   #value_counts 直接用来计算series里面相同数据出现的频率
# print(ss.describe())

