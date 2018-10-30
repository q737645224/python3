import pandas as pd
import numpy as np
# 1.Series创建
s1=pd.Series(data=[3,-5,7,4],index=list('abcd'))
print(s1)
# 2.DataFrame创建
data=[['Belglum','Brussels',11190846],
      ['Indla','New Delhi',1303171035],
      ['Brazil','Brasilia',207847528]]
# 比利时 布鲁塞尔
# 印度 新德里
# 巴西 巴西利亚
df=pd.DataFrame(data=data,index=[1,2,3],
                columns=['Country','Capital','Population'])
print(df)

