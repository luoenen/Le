'''
@ project: Le
@ file: test
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/25 20:17
'''
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
from imp import reload
import time
import json

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '65fbd9a9c760eaf4'
APP_SECRET = '0YZmwphie3hdHiA4XXYateyw42oVO8MQ'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(txt):
    q = txt

    data = {}
    data['from'] = 'en'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    dict = json.loads(response.content)
    return dict['translation'][0]