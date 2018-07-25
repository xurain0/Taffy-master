#conding=utf-8
import platform
import paramiko
import os

def TestPlatform():
    print '......Current Operation System.......'
    return platform.system()
print TestPlatform()

Host = '172.24.118.10'
Username = 'uapp'
Password = 'Sfituser_123'
Port = 22
#curr =  os.path.dirname(__file__)
local_dir = os.path.dirname(__file__)
# print local_dir
# remote_dir = '/home/uapp/zzz'
# print remote_dir
# transport = paramiko.Transport(('172.24.118.10', 22))
# transport.connect(username='uapp', password='Sfituser_123')
#
# sftp = paramiko.SFTPClient.from_transport(transport)
# files = os.listdir(local_dir)
# print files
# sftp.put(r'C:\Users\xu.ren\Desktop\cfmmc_N_20180103_00000001.xml', '/home/uapp/zzz/cfmmc_N_20180103_00000001.xml')
# transport.close()
# local_dir = os.path.dirname(__file__)
# print local_dir
# remote_dir = '/home/uapp/zzz'
# print remote_dir
# client = paramiko.Transport((Host, Port))
# client.connect(username=Username, password=Password)
# sftp = paramiko.SFTPClient.from_transport(client)
# files = sftp.listdir(remote_dir)
# for f in files:
#     print 'Uploading file :', os.path.join(local_dir, f)
#     sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))
#     print 'Uploading file success'

#sftp.put('*.py', '/home/uapp/zzz/*.py')
#sftp.get('/home/uapp/shell/bns.sh', 'D:/')

#client.close()
#class linuxConnect(object):
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(Host, Port, Username, Password)
# stdin, stdout, stderr = ssh.exec_command('. ~/shell/setenv.sh ; ls')
# out = stdout.readlines()
# print out
# hostname='172.24.118.9'
# username='uapp'
# password='Sfituser_123'
# port=22
# local_dir=os.path.dirname(__file__)
# remote_dir='/home/uapp/zzz'
# print local_dir + "1"
# transport = paramiko.Transport(('172.24.118.9', 22))
# transport.connect(username='uapp', password='Sfituser_123')
# sftp=paramiko.SFTPClient.from_transport(transport)
# files=sftp.listdir(local_dir)
# print files
# try:
#     print local_dir
#     transport = paramiko.Transport(('172.24.118.9', 22))
#     transport.connect(username='uapp', password='Sfituser_123')
#     sftp=paramiko.SFTPClient.from_transport(transport)
#     files=sftp.listdir(local_dir)
#     print local_dir
#     #files=sftp.listdir(remote_dir)
#     for f in files:
#         print ''
#         print '#########################################'
#         #print 'Beginning to download file  from %s  %s ' % (hostname,datetime.datetime.now())
#         print 'Downloading file:',os.path.join(remote_dir,f)
#         #sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))
#         sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
#         #print 'Download file success %s ' % datetime.datetime.now()
#         print ''
#         print '##########################################'
#     t.close()
# except Exception:
#        print "connect error!"
def test():
    try:
        client = paramiko.Transport(('172.24.118.10', 22))
        client.connect(username=Username, password=Password)
        sftp = paramiko.SFTPClient.from_transport(client)
        print 'ffffffff'
        files = os.listdir(local_dir)
        print local_dir
        for f in files:
            print 'Uploading file :', os.path.join(local_dir, f)
            sftp.put(os.path.join(local_dir, f), os.path.join('/home/uapp/zzz', f))
            print 'Uploading file success'
        client.close()
    except Exception:
            print "connect error!"

test()

def uploadFiles(self):
    #ssh = sshUtils()
    ssh = ''
    local_dir = 'D:/testPlam/Taffy-master/Util/uaoUtilTool/'
    remote_dir = '/home/uapp/zzz'
    host = '172.24.118.9'
    restartCmd = '. ~/shell/setenv.sh ; . /home/uapp/zzz/uao.sh'
    getServiceIpCmd = '. ~/shell/setenv.sh ; cat /home/uapp/shell/console/execute.list | grep uao | awk \'NR==1{print $5}\''
    killUaoThreadCmd = '. ~/shell/setenv.sh ; . /home/uapp/zzz/exceUao.sh'
    exceIneUaoCmd = '. ~/shell/setenv.sh ; . /home/uapp/services/uao_ineuao1/bin/ineuao 1 -f cfmmc_N_20180522_00000001.xml'
    #restart uao service
    restart = ssh.connSsh(host, restartCmd)
    if restart[0] <> 0 :
        ret = "errcode=" + str(restart[0]) + ";" + "errmsg=" + str(restart[1])
    else:
        print restart[2] + "ccc"
        #get uap installed server ip
        getServiceIp = ssh.connSsh(host, getServiceIpCmd)
        if getServiceIp[0] <> 0 :
            ret = "errcode=" + str(getServiceIp[0]) + ";" + "errmsg=" + str(getServiceIp[1])
        else:
            print getServiceIp[2] + 'aaaa'
            #upload local files to remote
            ssh.uploadFiles(getServiceIp[2].strip(), local_dir, remote_dir)
            #kill uao thread
            killUaoThread = ssh.connSsh(getServiceIp[2].strip(), killUaoThreadCmd)
            print killUaoThread[2]
            exceIneUao = ssh.connSsh(getServiceIp[2].strip(), exceIneUaoCmd)
            if exceIneUao[0] <> 0 :
                ret = "errcode=" + str(exceIneUao[0]) + ";" + "errmsg=" + str(exceIneUao[1])
            else:
                print exceIneUao[2]
    return ret