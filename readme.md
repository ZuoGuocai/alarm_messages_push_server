## 功能介绍

统一报警消息API调用方法:支持GET,POST方法, 参数说明:key 你的key; bumen 部门id; msg要发送的消息                
示例1: 浏览器 http://172.168.110.110/send?key=abcd1234&bumen=2&msg=你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案</p>
示例2: curl -i -X POST -H "'Content-type':'application/json'" -d '{"key":"abcd1234","bumen":"2","msg":"你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案"}'  http://172.168.110.110/send

##  Test Demo
centos7上python2调用接口测试通过

```
#!/usr/bin/env python
#coding=utf-8
import urllib2
import json
    
def notice_push(message):
    url='http://172.168.110.110/send'
    values ={'key':'abcd1234','bumen':'2','msg':message}

    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)      # 生成页面请求的完整数据
    response = urllib2.urlopen(req)        # 发送页面请求
    return response.read()                 # 获取服务器返回的页面信息



my_msg='你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案'
resp = notice_push(my_msg)
print(resp)
```

```
#!/usr/bin/env python
#coding=utf-8
import urllib2
import json

class Send:    
  def __init__(self,message):
      self.message = message    
  def notice_push(self):
      url='http://172.168.110.110/send'
      values ={'key':'abcd1234','bumen':'2','msg':self.message}

      jdata = json.dumps(values)             # 对数据进行JSON格式化编码
      req = urllib2.Request(url, jdata)      # 生成页面请求的完整数据
      response = urllib2.urlopen(req)        # 发送页面请求
      return response.read()                 # 获取服务器返回的页面信息





if __name__ == '__main__':
  msg='你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案'
  obj = Send(msg)
  status = obj.notice_push()
  print(status)

```