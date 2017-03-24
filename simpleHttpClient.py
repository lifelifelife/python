# /usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import base64
import hashlib
import sys
import json

args = {
    "content": "俺的沙发 ",
    "goods_list": "",
    "item_list": "37:1;65:10;66:10",
    "item_param": "{\"1\":{},\"2\":{},\"3\":{}}",
    "level_end": "",
    "level_start": "",
    "memo": "",
    "res_list": "{\"hero_list\":\"\"}",
    "serverId": "1300430001",
    "server_id": "1300430001",
    "tag": "",
    "title": "阿发达地方",
    "type": "player_id",
    "user_list": "4311744731",
    "vip_level_end": "",
    "vip_level_start": ""
}

text = json.dumps(args)
secretKey = 'GMXGAME@#*UUZU2014'
query = text + secretKey
url = 'http://localhost:9494/gm'
if sys.version_info[0] >= 3:  # python 3.x
    encoded = base64.b64encode(bytes(text, 'utf-8'))
    query = query.encode('utf-8')
else:  # python 2.x
    encoded = base64.b64encode(text)
auth = hashlib.md5(query).hexdigest()
r = requests.post(url, data={'action': 'sendMail', 'data': encoded, 'auth': auth[5:25]})
print(r)
