#/usr/bin/env python
# -*- coding:utf-8 -*-
#***********************************************************************
#* Author        : zuoguocai
#* Email         : zuoguocai@126.com
#* Create time   : 2018年6月14日20:28:53
#* Last modified : 2018年6月14日20:28:59
#* Filename      : push_server.py
#* Description   : push alarm messages use http get methods via wechat
#*                 write with python3
#* *********************************************************************



from sanic import Sanic
from sanic import response
from send_wechat_py3 import *


app = Sanic()
@app.route('/')
async def handle_request(request):
  return response.html('<p>统一报警消息API调用方法:支持GET方法,http://172.16.110.110/send?access_token=你的token&msg=要发送的消息</p> <p>示例: curl http://172.20.110.110/send?access_token=abcd1234&msg=你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案</p>')

@app.route('/send',methods=['GET'])
async def handle_request(request):
  args1 = request.args.get('access_token')
  args2 = request.args.get('msg')
  token_members = ['1234abcd', '4321abcd', 'abcd1234']
  if args1 in token_members:
    obj = Weixin(url, corpid, corpsecret)
    obj.messages(args2)
    return response.json({'status':"success"})
  else:
    return response.json({'status':"access_token or msg is wrong,please check it"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
