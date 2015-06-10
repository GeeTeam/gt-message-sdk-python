#!coding:utf8
from hashlib import md5
import urllib2
from urllib import urlencode
import json


class geetest(object):
    """docstring for gt"""
    API_SERVER = "http://messageapi.geetest.com/"
    SEND = "send"
    VALIDATE = "validate"

    def __init__(self, id, key):
        self.PRIVATE_KEY = key
        self.MSG_ID = id
        self.PY_VERSION = "2.15.4.1.1"

    def send_request(self, challenge, validate, seccode, phone):
        apiserver = self.API_SERVER + self.SEND
        print apiserver
        if validate == self.md5value(self.PRIVATE_KEY + 'geetest' + challenge):
            data = {
                "seccode": seccode,
                "sdk": "python_" + self.PY_VERSION,
                'phone': phone,
                'msg_id': self.MSG_ID
            }
            res = self.postvalues(apiserver, data)
            return res['res']
        else:
            return -11

    def msg_validate(self, phone, code):
        apiserver = self.API_SERVER + self.VALIDATE
        data = {
            'phone': phone,
            'msg_id': self.MSG_ID,
            'code': code
        }
        res = self.postvalues(apiserver, data)
        return res

    def postvalues(self, apiserver, data):
        req = urllib2.Request(apiserver)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, urlencode(data))
        res = response.read()
        return json.loads(res)

    def md5value(self, values):
        m = md5()
        m.update(values)
        return m.hexdigest()
