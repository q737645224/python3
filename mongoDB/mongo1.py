from pymongo import MongoClient

conn = MongoClient("localhost",27017)

db = conn.stu 

myset = db.class4 

#索引操作
# index = myset.ensure_index('name')
# print(index)   #返回索引名称

#创建复合索引
# index = myset.ensure_index\
# ([('name',1),('King',-1)])

#创建唯一索引稀疏索引
# index = myset.ensure_index\
# ('King',unique = True,sparse = True)

#查看当前索引
# for i in myset.list_indexes():
#     print(i)

# #删除一个索引
# myset.drop_index('name_1')

# #删除所有索引
# myset.drop_indexes()

#聚合操作
l = [{'$group':{'_id':'$King','count':{'$sum':1}}},
    {'$match':{'count':{'$gt':1}}}
    ]

cursor = myset.aggregate(l)
for i in cursor:
    print(i)


conn.close()