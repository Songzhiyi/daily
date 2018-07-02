#! /usr/bin/env python
#coding=utf-8
#_Author_ = "songzhiyi"
#Author:songzhiyi
import requests                                 #导入requests包
# r=requests.get(url='http://127.0.0.1:8081/')
#requests.adapters.DEFAULT_RETRIES = 5
#content={'eq_id':10,'channel_type':4,'url':'null'}
content={'core_id':3,'eq_id':11,'channel_type':3,'size':720}
#r=requests.get('http://192.168.200.192:8080/crh_gt_live_webservice/stopTrainLiveUpload?equipmentNo=2&videoIndex=5&url=rtmp://111.1.11.11/live/name&type=1',params=content)
#r = requests.get('http://192.168.200.185:8089',params=content)
r = requests.get('http://192.168.200.201/nclients?app=live&name=1')
#print (r.url)
#获取请求内容
clients = int(r.text)#获取响应内容
if clients<1:
    print('当前用户为0，可以关闭直播!')
else:print("有%s个用户" %clients)