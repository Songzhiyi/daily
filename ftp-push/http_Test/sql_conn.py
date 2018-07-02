#! /usr/bin/env python
#coding=utf-8
#_Author_ = "songzhiyi"
#Author:songzhiyi
#coding = utf-8
import pymysql
import re
connect = pymysql.connect(
    user = 'root',
    password='mysql',
    host = '192.168.200.185',
    port = 3306,
    db = 'crh_gt_live',
    charset = 'utf8'
)
conn = connect.cursor() #操作游标
# conn.execute('SELECT * FROM USER ')

# conn.execute("create database new_database")
conn.execute("use crh_gt_live")
# sql = ''' create table new_table(Car_in BIGINT,Pipe_id BIGINT,Rate BIGINT,Port BIGINT,Route VARCHAR(20))'''
# conn.execute(sql)
path = '/?core_id=3&eq_id=1&channel_type=1&size=720'
# a = int(path[10])
# print(a)
# print(type(a))
core_id = re.findall('\d+',path)[0]
eq_id = re.findall('\d+',path)[1]
channel_type = re.findall('\d+',path)[2]

# core_id = num[0]
# print(core_id)
# sql = '''INSERT INTO s_media_control(eq_id,
#          channel_type,size,live_Port,route_url)
#           VALUES (%s, %s, 720, 1935, 'rtmp://192.168.185:1935/myapp/')''' %(eq_id,channel_type)
sql_2 = '''select * from s_media_control WHERE eq_id=10 AND channel_type=2 AND size=480'''
sql_3='''select count(*) from s_media_control '''
try:
    conn.execute(sql_3)
    # print("提交成功")
    #connect.commit()
    #conn.execute('SELECT * FROM s_media_control ')
    # row = conn.fetchall()
    # for j in row:
    #     print(j)
    # conn.execute('select * from s_media_control WHERE eq_id=10 AND channel_type=2 AND size=720')
    rows = conn.fetchall()
    for i in rows:
        print(1935-i[0]-1)
    conn.close()
    connect.close()
except Exception as e:
    print('error')