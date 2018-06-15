## 功能介绍

统一报警消息API调用方法:支持GET,POST方法, 参数说明:key 你的key; bumen 部门id; msg要发送的消息                
示例1: 浏览器 http://172.168.110.110/send?key=abcd1234&bumen=2&msg=你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案</p>
示例2: curl -i -X POST -H "'Content-type':'application/json'" -d '{"key":"abcd1234","bumen":"2","msg":"你知道我对你不仅仅是喜欢,你眼中却没有我想要的答案"}'  http://172.168.110.110/send