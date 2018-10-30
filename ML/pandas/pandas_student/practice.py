import numpy as np
import pandas as pd
# 创建DataFrame
df = pd.DataFrame([['Snow','M',22],['Tyrion','M',32],['Sansa','F',18],['Arya','F',14]], columns=['name','gender','age'])
print(df)
#选取多列，gender和age列
# print(df[['gender','age']])
# print(df.loc[:,['gender','age']])
# print(df.iloc[:,[1,2]])
# print(df.iloc[:,1:3])

#读取第1行到第2行的数据
# print(df[1:3])
# print(df.iloc[1:3])

#读取第1行和第3行，从第0列到第2列,不包括第二列
# print(df.iloc[[1,3],0:2])

#读取倒数第3行到倒数第1行的数据
# print(df[-3:-1])
print(df.iloc[-3:-1])


