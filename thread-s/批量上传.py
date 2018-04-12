_Author_ = "songzhiyi"
import os,sys
import paramiko
import threading
import netaddr
from optparse import OptionParser
usage = sys.argv[0] + " [选项]"
parser = OptionParser(usage)
parser.add_option('-a', '--host',
                  dest='host',
                  action='store',
                  default=False,
                  help='需要执行命令的主机，跟主机IP地址，多个IP用逗号分隔，也可以用“-”连接一个主机范围')
parser.add_option('-b', '--path',
                  dest='path',
                  action='store',
                  default=False,
                  help='上传的文件的路径，以及传入的路径，两者用逗号分隔')
options, args = parser.parse_args()

def ftp_put(ip,path1,path2):
    private_key = paramiko.RSAKey.from_private_key_file('/home/.ssh/id_rsa')
    transport = paramiko.Transport((ip,22))
    transport.connect(username = 'root', pkey=private_key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(path1, path2)
    transport.close()
if __name__ == '__main__':

    if not options.host:
        print("请指定主机")
        exit(1)
    if not options.path:
        print("请输入路径!")
    path = options.path.split(',')
    path1 = path[0]
    path2 = path[1]
    if ',' in options.host:
        ip = options.host.split(',')
        for i in ip:
            t = threading.Thread(target=ftp_put(), args=(i,path1,path2))  # 使用线程方式执行，更快
            t.start()
    elif '-' in options.host:
        startip = options.host.split('-')[0]
        endip = options.host.split('-')[1]
        ip = list(netaddr.IPRange(startip, endip))  # netaddr.IPRange()用于计算IP地址区间内的所有IP
        for i in ip:
            t = threading.Thread(target=ftp_put(), args=(str(i), path1,path2))
            t.start()
    else:
        ip = options.host
        ftp_put(ip,path1,path2)