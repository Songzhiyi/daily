#! /usr/bin/env python
#coding=utf-8
#_Author_ = "songzhiyi"
import os,sys
import pymysql
import requests    #导入requests包
import time
# r=requests.get(url='http://127.0.0.1:8081/')
# requests.adapters.DEFAULT_RETRIES = 5
#                       #获取响应内容
while True:
    connect = pymysql.connect(
        user = 'root',
        password='song192625',
        host = '192.168.1.3',
        port = 3306,
        db = 'MYSQL',
        charset = 'utf8'
    )
    conn = connect.cursor() #操作游标
    conn.execute('use crh_gt_live')
    rows = conn.fetchall()
    conn.execute('select * from s_media_control ')
    for i in rows:
        port=i[3]
        code = os.system("netstat -anotup|grep %s|awk 'END{print NR}'" % port)  # 读出连接到端口的个数
        if code<2:
            content = {'eq_id': i[0], 'channel_type': i[1], 'url':i[4]}
            r=requests.get('http://192.168.200.192:8080/crh_gt_live_webservice/stopTrainLiveUpload?equipmentNo=2&videoIndex=5&url=rtmp://111.1.11.11/live/name&type=1',params=content)
            print (r.url)                       #获取请求内容
            print (r.text)
    conn.close()
    connect.close()
    time.sleep(30)