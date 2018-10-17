from pymongo import MongoClient 
#和pymongo 绑定 
import gridfs

conn = MongoClient('localhost',27017)
db = conn.grid 

#获取gridfs 对象  
#fs拥有fs.files fs.chunks两者的属性
fs = gridfs.GridFS(db)

#生成文件游标
files = fs.find()

#获取每一个文件
for file in files:
    print(file.filename)
    if file.filename == 'file.jpg':
        with open(file.filename,'wb') as f:
            #从数据库读取文件
            data = file.read()
            #写入到本地
            f.write(data)
            
conn.close()
