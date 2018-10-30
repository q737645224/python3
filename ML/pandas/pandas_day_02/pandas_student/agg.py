import pandas as pd
import numpy as np
#给定以下数据
df = pd.DataFrame({'A': [1, 1, 2, 2],
                   'B': [1, 2, 3, 4],
                   'C': np.random.randn(4)})
print(df)
# 按照A列分组后聚合求最小值 df1接收

# 按照A列分组后聚合求最小值和最大值 df2接收

# 按照A列分组后聚合后对B列求最小值和最大值，对C列求和，df3接收
