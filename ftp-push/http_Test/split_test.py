#! /usr/bin/env python
#coding=utf-8
#_Author_ = "songzhiyi"
import re
#Core_Id=10,carid=19,pipeid=29
path = '/?core_id=3&eq_id=1&channel_type=1&size=720'
# a = int(path[10])
# print(a)
# print(type(a))
core_id = re.findall('\d+',path)[0]
eq_id = re.findall('\d+',path)[1]
channel_type = re.findall('\d+',path)[2]
size = re.findall('\d+',path)[3]
# core_id = num[0]
# print(core_id)
print(type(core_id))
print(eq_id)
print(channel_type)
print(size)
i = 3
q=100-1-i
print(q)