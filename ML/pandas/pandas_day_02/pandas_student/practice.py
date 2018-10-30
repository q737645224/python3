import numpy as np
import pandas as pd
# 创建DataFrame
df = pd.DataFrame([['Snow','M',22],['Tyrion','M',32],['Sansa','F',18],['Arya','F',14]], columns=['name','gender','age'])
print(df)
#选去多列，gender和age列
# print(df[['name','gender']])
# print(df.loc[:,['name','gender']])
# print(df.iloc[:,[0,1]])
# print(df.iloc[:,0:2])

#读取第1行到第2行的数据
# print(df[1:3])
# print(df.iloc[1:3])

#读取第1行和第3行，从第0列到第2列,不包括第二列
# print(df.iloc[[1,3],0:2])

#读取倒数第3行到倒数第1行的数据
# print(df[-3:-1])


print('本节课内容')
df1=df.copy()
print(df1)


# 给上个例子学生加上score一列。分别为：80，98，67，90



# 在gender后面加一列城市

# list.insert(index, obj)
# index -- 对象 obj 需要插入的索引位置。
# obj -- 要插入列表中的对象






# 给上个例子学生加上一行信息
#首先，要创建一个DataFrame。要注意，在这里需加入index属性，lisa F 19 100

#然后，开始插值。ignore_index=True,可以帮助忽略index，自动递增。

#最重要的，赋值给df1





print('删除功能练习')
# # 删除第0行



# # 删除第score列


# 对score列排序





