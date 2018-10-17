from pymongo import MongoClient 
#pymongo 附带
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.images 
myset = db.img  

# #存储
# f = open('file.jpg','rb')

# #转换为mongo能存储的格式
# content = bson.binary.Binary(f.read())

# myset.insert\
# ({'filename':'file.jpg','data':content})

#取出文件
data = myset.find_one({'filename':'file.jpg'})

#读取内容写入本地
with open(data['filename'],'wb') as f:
    f.write(data['data'])


conn.close()
