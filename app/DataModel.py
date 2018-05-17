from app import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=False)
    email=db.Column(db.String(80),unique=True)


    def __repr__(self):
        return "User %s ，email %s"%self.username,self.email

