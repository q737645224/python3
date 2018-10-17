# 创建一张表

# 连接数据库的模块
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql://root:123456@localhost/db4",encoding="utf8")
Base = declarative_base() # orm基类

class User(Base): # 继承Base基类
    __tablename__ = "t123"
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    address = Column(String(40))

Base.metadata.create_all(engine)








