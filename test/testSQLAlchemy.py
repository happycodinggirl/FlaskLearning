# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
#engine = create_engine('mysql+mysqlconnector://lily:hxl0615:@eimkcvtfohdx.mysql.sae.sina.com.cn:10642/userdb_1')
engine = create_engine('mysql+mysqlconnector://qdm226570533:jiangfuqi:@qdm226570533.my3w.com:3306/qdm226570533_db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
