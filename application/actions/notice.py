# -*- coding: utf-8 -*-
# !/usr/bin/env python

import json
import requests

def callme(text):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "通知",
            "text": text
        }
    }
    print(data)
    r = requests.post('https://oapi.dingtalk.com/robot/send?access_token=c7c1a842ffd7ee6cae3c41c10fb7ab5f029692c810eb232e106cad3c47b0cdc7', data=json.dumps(data), headers=headers)
    print(r.url)
    print(r.status_code)

