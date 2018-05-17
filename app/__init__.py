from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://qdm226570533:jiangfuqi@qdm226570533.my3w.com/qdm226570533_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://qdm226570533:jiangfuqi@w.rdc.sae.sina.com.cn:3307/qdm226570533_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mm2y3mx25o:20yx0hw4i40lkkyxklhhx5wxk5m1w5zkhlw13ylk@eimkcvtfohdx.mysql.sae.sina.com.cn:10642/userdb_1'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mm2y3mx25o:20yx0hw4i40lkkyxklhhx5wxk5m1w5zkhlw13ylk@w.rdc.sae.sina.com.cn:3306/app_happycodinggirl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

if __name__=="__main__":
        print("init hahah ")
        db.create_all()



