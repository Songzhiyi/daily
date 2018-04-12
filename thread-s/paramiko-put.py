# -*- coding:utf-8 -*-
import paramiko
hosts = ['192.168.200.235']
for host in hosts:
    def sftp_upload_file(server_path, local_path):
        try:
            t = paramiko.Transport((host, 22))
            t.connect(username='root', password='srddrs')
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put(server_path, local_path)
            t.close()
        except Exception as e:
            print (e)
if __name__ == '__main__':
    sftp_upload_file("D:\Documents\Desktop\login.py", "/home/login.py")
    #sftp_upload_file("/root/", "D:\Documents\Desktop\login.py")