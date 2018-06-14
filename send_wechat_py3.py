#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import json
import sys
import logging



touser = '@all'
agentid = '1000004'
corpid = '你的企业微信corpid'
corpsecret = '你的企业微信corpsecret'
url = 'https://qyapi.weixin.qq.com'
message = ''

logging.basicConfig(level=logging.DEBUG, filename='/var/log/wechat.log',
                    format='%(asctime)s - %(levelname)s: %(message)s')


class Weixin:
    def __init__(self, url, corpid, corpsecret):
        token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
        self.token = json.loads(urllib.request.urlopen(token_url).read().decode())['access_token']

    def send_message(self, url, data):
        send_url = '%s/cgi-bin/message/send?access_token=%s' % (url, self.token)
        self.respone = urllib.request.urlopen(urllib.request.Request(url=send_url, data=data)).read()
        x = json.loads(self.respone.decode())['errcode']

        if x == 0:
            logging.debug('Successfully %s' % ( message))
            return 'Succesfully'
        else:
            logging.debug('Failed %s' % ( message))
            return 'Failed'

    def messages(self, message):
        values = {
            "touser": touser,
            "msgtype": 'text',
            "agentid": agentid,
            "text": {'content': message},
            "safe": 0
        }
        return self.send_message(url, bytes(json.dumps(values), 'utf-8'))



