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



html_template='''<p>统一报警消息API调用方法:支持GET,POST方法, 参数说明:key 你的key; bumen 部门id; msg要发送的消息</p>                 
                        <p>示例1: 浏览器 http://172.168.110.110/send?key=abcd1234&bumen=2&msg=你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案</p>
                        <p>示例2: curl -i -X POST -H "'Content-type':'application/json'" -d '{"key":"abcd1234","bumen":"2","msg":"你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案"}'  http://172.168.110.110/send                         </p>'''
token_members = ['1234abcd', '4321abcd', 'abcd1234']
obj = Weixin(url, corpid, corpsecret)



app = Sanic()
@app.route('/')
async def handle_request(request):
  return response.html(html_template) 

@app.route('/send',methods=['GET'])
async def handle_request(request):
  args1 = request.args.get('key')
  args2 = request.args.get('bumen')
  args3 = request.args.get('msg')
  if args1 in token_members:
    obj.messages(args2,args3)
    return response.json({'status':"success"})
  else:
    return response.json({'status':"error",'notice':"Your key,bumen or msg is invaild,please check it"})

@app.route('/send',methods=['POST'])
async def handle_request(request):
  args1 = request.json.get('key')
  args2 = request.json.get('bumen')
  args3 = request.json.get('msg')
  if args1 in token_members:
    obj.messages(args2,args3)
    return response.json({'status':"success"})
  else:
    return response.json({'status':"error",'notice':"Your key,bumen or msg is invaild,please check it"})






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
