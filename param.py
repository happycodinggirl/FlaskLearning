from flask import Flask
from flask import jsonify
from flask import abort

app=Flask(__name__)

userInfo=[{"name":"lily","age":18,"userId":1},{"name":"lucy","age":20,"userId":2}]


@app.route("/api/v1.0/getInfo/<int:userId>",methods=["GET"])
def getInfo(userId):
    isMap=type(userInfo) == type({})
    print("----isMap is ",isMap)
    #注意此处括号的使用，不加括号不对
    #python3filter函数不直接输出结果，需要list一下才会将结果转为list
    user=filter(lambda u:u["userId"]==userId,userInfo)
    result=list(user)
    print("-result is ",result," length is ",len(result))
    if len(result)==0:
        abort(404)

    return jsonify(result)




if __name__=="__main__":
    app.run(debug=True)


#使用方法浏览器输入http://127.0.0.1:5000/api/v1.0/getInfo/2，其中2是参数，获取userId==2的参数
#或者用curl -i http://127.0.0.1:5000/api/v1.0/getInfo/2 查看返回结果
