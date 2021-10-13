# -*-coding = utf-8 -*-
# @Time:2021/10/11/13:05
# @Author:seven
# @File:动态获取.py
# @Software:PyCharm
import requests
import re
import os
import json
import 神秘代码转数字 as sm
# url='https://space.bilibili.com/645741164/dynamic'
# url='https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=645741164&host_uid=645741164&offset_dynamic_id=0&need_top=1&platform=web'
url='https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=37663924&offset_dynamic_id=0&need_top=1&platform=web'
html=requests.get(url=url)
dt=html.json()['data']['cards'][4]['card']
Dt=json.loads(dt)
# print(Dt)
try:
    demo=Dt['item']['content']
    findlink = re.compile(r'【(.*?)】')
    en = re.findall(findlink, demo)
    ys=''
    jg=''
    for i in en:
        a = sm.cookie(i)
        ys+=a
        ys+=';'
        jg+=str(eval(a))
        jg+=';'
    print('原文爬取：',demo)
    print('----------------------------------')
    print('正则提取：',en)
    print('----------------------------------')
    print('原式：',ys)
    print('----------------------------------')
    print('口令：',jg)

except:
    demo=Dt['title']
    print('半佛发新视频了:',demo)

