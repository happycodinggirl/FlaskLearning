# -*- coding: utf-8 -*-

# filename: weixin.py

from flask import Flask, request, make_response

import time, hashlib

app = Flask(__name__)


@app.route('/wechat/', methods=['GET', 'POST'])

def wechat():

    # 微信验证token

    if request.method == 'GET':

        token = 'qfztwgxnadsipb8'

        query = request.args

        signature = query.get('signature', '')

        timestamp = query.get('timestamp', '')

        nonce = query.get('nonce', '')

        echostr = query.get('echostr', '')

        s = [timestamp, nonce, token]

        s.sort()

        s = ''.join(s)
        s=s.encode("utf8")
        sha1=hashlib.sha1(s)


        if sha1.hexdigest() == signature:
            return echostr

        return "faile"


if __name__=="__main__":
    app.run(debug=True)

