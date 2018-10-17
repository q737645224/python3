from pymongo import MongoClient

#创建数据库链接
conn = MongoClient("localhost",27017)

#创建数据库对象
db = conn.stu 
# db = conn['stu']

#获得集合对象
myset = db.class4 
# myset = db['class4']

#数据库增删改查
# print(dir(myset))

#插入操作
# myset.insert({'name':'张铁林','King':'乾隆'})
# myset.insert([{'name':'张国立','King':'康熙'},\
#     {'name':'陈道明','King':'康熙'}])
# myset.insert_many([{'name':'唐国强','King':'雍正'},\
#     {'name':'陈建斌','King':'雍正'}])
# myset.insert_one({'name':'郑少秋','King':'乾隆'})
# myset.save({'name':'吴奇隆','King':'四爷'})

#查找操作
# cursor = myset.find({},{'_id':0})

#i为每条文档转换的字典
# for i in cursor:
#     print(i['name'],"----",i['King'])

# myset = db.class1 

# cursor = myset.find({'age':{'$gt':17}},{'_id':0})
# for i in cursor:
#     print(i)
# print(cursor.next())
# print(cursor.count())
# print(cursor.limit(2))
# print(cursor.skip(2))
# for i in cursor.sort([('age',-1),('name',1)]):
#     print(i)

# dic = {'$or':[{'gender':'m'},{'age':{'$lt':18}}]}
# data = myset.find_one(dic,{'_id':0})
# print(data)

#修改操作
# myset.update({'name':'张国立'},\
#     {'$set':{'name':'国立'}})

#当要修改文档不存在的时候插入
# myset.update({'name':'冰冰'},\
#     {'$set':{'King':'武则天'}},upsert = True)

#可以同时修改多条文档
# myset.update({'King':'康熙'},\
#     {'$set':{"king_name":'玄烨'}},multi = True)

#删除操作
# myset.remove({'name':'冰冰'})

# myset.remove({'King':'康熙'},multi = False)

#查找并删除.返回查找到的文档字典
print\
(myset.find_one_and_delete({'King':'四爷'}))

#关闭数据库链接
conn.close()