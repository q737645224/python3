import pandas as pd
# 读取用户表
users = pd.read_table('users.dat',header=None,names=['UserID','Gender','Age','Occupation','Zip-code'], sep='::',engine= 'python')
# print(users.head())
# 读取评分表
ratings=pd.read_table('ratings.dat',header=None,names=['UserID', 'MovieID', 'Rating', 'Timestamp'],sep='::',engine='python')
# print(ratings.head())
# 读取电影详情表
movies=pd.read_table('movies.dat',header=None,names=['MovieID', 'Title', 'Genres'] ,sep='::',engine='python')
# print(movies.head())
# 将表进行合并

# 使用pivot_table方法 查看每一部电影不同性别的平均评分

