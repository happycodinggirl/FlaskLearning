from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xxxx:xxxx.my3w.com/xxxx_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

if __name__=="__main__":
        print("init hahah ")
        db.create_all()



