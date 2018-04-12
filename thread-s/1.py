_Author_ = "songzhiyi"
import paramiko
def ssh_login(ip, commond):
    "登录并执行命令，可以更改为使用密钥登录"
    private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username='root', pkey=private_key)
    stdin, stdout, stderr = ssh.exec_command(commond)
    print('%s\t%s' % (ip, stdout.read().decode()))
    # count = len(stdout)
    # while count>0:
    #     print (stdout.readline())
    #     count-=1
    ssh.close()
ssh_login('192.168.200.253','ifconfig')