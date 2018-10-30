import pandas as pd
import numpy as np
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)
# data1列数据，按key1来进行分组


# 一次传入多个数组 按照key1，key2分组计算

# 可以将列名（可以是字符串、数字或其他Python对象）用作分组


