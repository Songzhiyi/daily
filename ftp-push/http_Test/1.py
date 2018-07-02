#Author:songzhiyi
#!/usr/bin/python
#!/usr/bin/env python
#version=6.25
from http.server import BaseHTTPRequestHandler, HTTPServer
import pymysql
import os,sys
import re
import requests
 #划分两百个端口号50*4作为直播端口

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
    def do_GET(self):
        print(self.path)
        core_id = re.findall('\d+',self.path)[0]  #用正则取出str类型的core_id,此处是判断的关键
        if core_id=='1':
            eq_id = re.findall('\d+',self.path)[1]
            channel_type = re.findall('\d+',self.path)[2]
            if channel_type=='1' or channel_type=='4':
                #size = int(self.path[40:43])
                connect = pymysql.connect(
                     user='root',
                     password='mysql',
                     host='192.168.200.185',
                     port=3306,
                     db='crh_gt_live',
                     charset='utf8'
                  )  #连接到mysql的实例
                conn = connect.cursor() #操作游标
                conn.execute("use crh_gt_live")
                # conn.execute('select count(*) from s_media_control')
                # rows = conn.fetchall()
                # for i in rows:
                #     num=i[0]
                # live_port = 1935 - num
                # if num>300:
                #     self.send_response(200)
                #     self.send_header('Content-type', 'text/html')
                #     self.end_headers()
                #     self.wfile.write(bytes('0', "utf-8")) #如果端口不够用了。。。
                route_url="rtmp://192.168.200.185:1935/live/%s_%s" %(eq_id,channel_type)
                sql = ''' INSERT INTO s_media_control(eq_id,channel_type,size,live_port,route_url)VALUES (%s,%s,480,1935,'%s')''' %(eq_id,channel_type,route_url)
                conn.execute(sql)
                connect.commit()
                conn.execute('SELECT * FROM s_media_control ')
                conn.close()
                connect.close()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes('1', "utf-8"))
                print(route_url)
            elif channel_type=='2' or channel_type=='3':
                # size = int(self.path[40:43])
                connect = pymysql.connect(
                    user='root',
                    password='mysql',
                    host='192.168.200.185',
                    port=3306,
                    db='crh_gt_live',
                    charset='utf8'
                )  # 连接到mysql的实例
                conn = connect.cursor()  # 操作游标
                conn.execute("use crh_gt_live")
                # conn.execute('select count(*) from s_media_control ')
                # rows = conn.fetchall()
                # for i in rows:
                #     num = i[0]
                # live_port = 1935 - num
                # live_port_4 = 1935-num-1
                # if num > 300:
                #     self.send_response(200)
                #     self.send_header('Content-type', 'text/html')
                #     self.end_headers()
                #     self.wfile.write(bytes('0', "utf-8")) # 如果端口不够用了。。。
                route_url = "rtmp://192.168.200.185:1935/live/%s_%s" % (eq_id,channel_type)
                sql = ''' INSERT INTO s_media_control(eq_id,channel_type,size,live_port,route_url)VALUES (%s,%s,720,1935,'%s')''' % (
                eq_id, channel_type,route_url)
                conn.execute(sql)
                connect.commit()
                conn.execute('SELECT * FROM s_media_control ')
                route_url_4 = "rtmp://192.168.200.185:1935/live/%s_%s_480" % (eq_id,channel_type)
                sql_4 = ''' INSERT INTO s_media_control(eq_id,channel_type,size,live_port,route_url)VALUES (%s,%s,480,1935,'%s')''' % (
                    eq_id, channel_type,route_url_4)
                conn.execute(sql_4)
                connect.commit()
                conn.execute('SELECT * FROM s_media_control ')
                # route_url_4 = "rtmp://192.168.200.185:1935/live/%s" % (live_port_4)
                conn.close()
                connect.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('1', "utf-8"))
                print(route_url)
                print(route_url_4)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('error channel_type', "utf-8"))
        elif core_id=='2':   #暂不提供直接删除mysql中的数据，收到指令回复1，假装删除。
            try:
                eq_id = re.findall('\d+',self.path)[1]
                channel_type = re.findall('\d+',self.path)[2]
                #size = int(self.path[40:43])
                connect = pymysql.connect(
                     user='root',
                     password='mysql',
                     host='192.168.200.185',
                     port=3306,
                     db='crh_gt_live',
                     charset='utf8'
                  )  #连接到mysql的实例
                conn = connect.cursor()  # 操作游标
                conn.execute("use crh_gt_live")
                sql = " DELETE FROM s_media_control WHERE eq_id=%s AND channel_type=%s" %(eq_id,channel_type)
                conn.execute(sql)
                connect.commit()
                conn.execute('SELECT * FROM s_media_control ')
                conn.close()
                connect.close()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes('1', "utf-8"))
            except Exception as e:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('0', "utf-8"))
        elif core_id=='3':
            eq_id = re.findall('\d+',self.path)[1]
            channel_type = re.findall('\d+',self.path)[2]
            size = re.findall('\d+',self.path)[3]
            if size=='720':
                connect = pymysql.connect(
                     user='root',
                     password='mysql',
                     host='192.168.200.185',
                     port=3306,
                     db='crh_gt_live',
                     charset='utf8'
                  )  #连接到mysql的实例
                conn = connect.cursor()  # 操作游标
                conn.execute("use crh_gt_live")
                conn.execute(" SELECT * FROM s_media_control WHERE eq_id=%s AND channel_type=%s AND size=720" %(eq_id,channel_type))
                rows = conn.fetchall()
                for i in rows:
                    m = i[4]
                conn.close()
                connect.close()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                try:
                    self.wfile.write(bytes(m, "utf-8"))
                except Exception as e:
                    self.wfile.write(bytes('0', "utf-8")) #无法开启直播，id异常
            elif size=='480':
                if channel_type=='1' or channel_type=='4':
                    connect = pymysql.connect(
                        user='root',
                        password='mysql',
                        host='192.168.200.185',
                        port=3306,
                        db='crh_gt_live',
                        charset='utf8'
                    )  # 连接到mysql的实例
                    conn = connect.cursor()  # 操作游标
                    conn.execute("use crh_gt_live")
                    conn.execute(
                        " SELECT * FROM s_media_control WHERE eq_id=%s AND channel_type=%s" % (eq_id, channel_type))
                    rows = conn.fetchall()
                    for i in rows:
                        m = i[4]
                    conn.close()
                    connect.close()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    try:
                        self.wfile.write(bytes(m, "utf-8"))
                    except Exception as e:
                        self.wfile.write(bytes('0', "utf-8"))  # 无法开启直播，id异常
                elif channel_type=='2' or channel_type=='3':
                    connect = pymysql.connect(
                        user='root',
                        password='mysql',
                        host='192.168.200.185',
                        port=3306,
                        db='crh_gt_live',
                        charset='utf8'
                    )  # 连接到mysql的实例
                    conn = connect.cursor()  # 操作游标
                    conn.execute("use crh_gt_live")
                    conn.execute(
                        " SELECT * FROM s_media_control WHERE eq_id=%s AND channel_type=%s AND size=720" % (eq_id, channel_type))
                    rows = conn.fetchall()
                    for i in rows:
                        m = i[4]
                    r = requests.get('http://192.168.200.192:8080/crh_gt_live_webservice/stopTrainLiveUpload?equipmentNo=2&videoIndex=5&url=rtmp://111.1.11.11/live/name&type=1'
                                     ,params=m)  #将需要车载推送的url发送给控制
                    if r.text=='1':
                        conn.execute(
                            " SELECT * FROM s_media_control WHERE eq_id=%s AND channel_type=%s AND size=480" % (eq_id, channel_type))
                        row = conn.fetchall()
                        for j in row:
                            k = j[4]
                        conn.close()
                        connect.close()
                        os.system('ffmpeg -re -i %s -vcodec libx264 -acodec aac -b 500k -s 640*480 -r 25 -f flv %s' %(m,k))
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        try:
                            self.wfile.write(bytes(k, "utf-8"))
                        except Exception as e:
                            self.wfile.write(bytes('0', "utf-8"))  # 无法开启直播，id异常
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('0', "utf-8"))


        elif core_id=='5':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('0', "utf-8"))
        elif core_id=='6':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('0', "utf-8"))
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('0', "utf-8"))
            print("argument error")

        # # Send response status code
        # self.send_response(200)
        # # # Send headers
        # self.send_header('Content-type','text/html')
        # self.end_headers()
        # # # Send message back to client
        # message = "1"
        # # # Write content as utf-8 data
        # self.wfile.write(bytes(message, "utf-8"))
        return

def run():
    print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('192.168.200.139', 8089)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()



run()