from flask import make_response
from flask import jsonify
from flask import request
from app import app,db
from app.DataModel import User



def hasInTable(name):
    for user in db.session.query(User):
        if user.username==name:
            return True

    return False

@app.route("/regist/",methods=['POST'])
def regist():
    print("---form name is ",request.form.get("name"),"email is ",request.form.get("email"))
    if hasInTable(request.form.get("name")):
       return make_response(jsonify({"msg":"user has regist","code":101}))
    else:
        newUser=User(username=request.form.get("name"),email=request.form.get("email"))
        db.session.add(newUser)
        db.session.commit()
        return make_response(jsonify({"msg":"regist sucess","code":100}))



if __name__=="__main__":
    print("regist main")
    app.run(debug=True)

