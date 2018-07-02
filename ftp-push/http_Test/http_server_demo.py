#! /usr/bin/env python
#coding=utf-8
#_Author_ = "songzhiyi"
from http.server import BaseHTTPRequestHandler, HTTPServer
import pymysql
import os,sys
import io,shutil,urllib
import requests

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
    def do_GET(self):
        print(self.path)
        content = {'core_id':3,'eq_id':2,'channel_type':2,'size':720}
        r = requests.get('http://192.168.200.185:8089', params=content)
        if r.text=='1':
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send message back to client
            message = "1"
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf-8"))

        else:
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send message back to client
            message = "0"
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf-8"))

def run():
    print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('192.168.200.136', 8000)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()
run()
