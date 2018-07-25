# -*- coding: utf-8 -*-
'''
Created on 2018-05-16
@author : xu.ren
'''

import paramiko
import datetime
import os

class sshUtils(object):
    username = 'uapp'
    password = 'Sfituser_123'
    def connSsh(self, host, cmd):
        code = 0
        errmsg = ""
        status = ""
        try:
            paramiko.util.log_to_file('paramiko.log')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=self.username, password=self.password)
            stdin, stdout, stderr=ssh.exec_command(cmd)
            status = ""
            errmsg = ""
            for out in stdout:
                status = status + out
            for out in stderr:
                errmsg = errmsg + out
            ssh.close()

        except Exception, e:
            errmsg = e.args[0]
            code = -1
        return code, errmsg, status

    def uploadFiles(self, host, local_dir, remote_dir, date):
        #将xml文件名改为含有当日date的文件名
        for root, dirs, files in os.walk(local_dir):
            oldname = files
            newname = []
            for i in oldname:
                i = i.replace(i[8:16], date)
                newname.append(i)
            for n in range(len(newname)):
                os.rename(os.path.join(local_dir, oldname[n]), os.path.join(local_dir, newname[n]))
        #删除recv下当日的文件
        rmCmd = 'cd /home/uapp/services/uao_ineuao1/recv/ ; rm -r *' + date + '*'
        self.connSsh(host, rmCmd)
        print 'rm -r *' + date + '*'

        #上传文件至recv下
        try:
            print 'upload files to :', host, ' dir :', remote_dir
            client = paramiko.Transport((host, 22))
            client.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(client)
            files = os.listdir(local_dir)
            for f in files:
                print 'Uploading file :', os.path.join(local_dir, f), 'to ', host, ':/home/uapp/services/uao_ineuao1/recv/'
                sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))
                print 'Uploading file success'
            client.close()
        except Exception:
            print "connect error!"

# local_dir = 'D:/testPlam/Taffy-master/Util/uaoUtilTool'
# remote_dir = '/home/uapp/zzz'
# host = '172.24.118.10'
# date = '20180622'
# local_dir = 'D:/testPlam/Taffy-master/Data/organAccount/'
# remote_dir = '/home/uapp/services/uao_ineuao1/recv/'
# s = sshUtils()
# s.uploadFiles(host, local_dir, remote_dir, date)


