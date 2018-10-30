import pandas as pd
import numpy as np
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)
# 练习1
# # 任何长度适当的数组
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])



# 练习2
# # 通过字典或Series进行分组
people = pd.DataFrame(np.random.randn(5, 5),
       columns=['a', 'b', 'c', 'd', 'e'],
       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis']
 )
print(people)
mapping = {'a':'red', 'b':'red', 'c':'blue',
         'd':'blue', 'e':'red'}




