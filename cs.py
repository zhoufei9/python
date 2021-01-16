# -*- coding: utf-8 -*-
import json
import requests
from urllib.parse import urlencode

headers = {"Content-Type": "application/json"}

# 消息类型和数据格式参照钉钉开发文档
data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "通知首屏会话透出的展示内容",
        "text": "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n ![alt 啊](https://gw.alipayobjects.com/zos/skylark-tools/public/files/b424a1af2f0766f39d4a7df52ebe0083.png)"
    }
}

r = requests.post('https://oapi.dingtalk.com/robot/send?access_token=c7c1a842ffd7ee6cae3c41c10fb7ab5f029692c810eb232e106cad3c47b0cdc7', data=json.dumps(data), headers=headers)
