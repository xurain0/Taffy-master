# -*- coding: utf-8 -*-
'''
Created on 2018-05-22

@author: xu.ren
'''

from Util import *
import json


class uao(object):
    backInfoPath = 'D:/testPlam/Taffy-master/config/backInfo.xml'
    local_dir = 'D:/testPlam/Taffy-master/config/openAccountData/'
    remote_dir = '/home/uapp/zzz/'
    host = '172.24.118.9'
    cmd = xmlUtils()
    ssh = sshUtils()
    x2j = xml2jsonUtils()
    o2j = oracle2jsonUtils()
    orcl = orclUtils()
    com = compareFiles()

    def getValue(self, sql):
        data = self.orcl.connOrcl(sql)
        for row in data[2]:
            for r in row:
                value = r
                print value
        return value

    def test_reStartUaoJob(self):
        restartUaoCmd = self.cmd.readXml('restartUao', self.backInfoPath)
        restart = self.ssh.connSsh(self.host, restartUaoCmd)
        if restart[0] <> 0:
            ret = "errcode=" + str(restart[0]) + ";" + "errmsg=" + str(restart[1])
        else:
            ret = restart[2]
        print ret

    def test_uploadXmlFiles(self):
        ora = orclUtils()
        findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
        findSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'cfmmc\''
        inMaxNo = ora.connOrcl(findinMaxNosql)[2]
        seqNo = ora.connOrcl(findSeqNosql)[2]
        getRemoteServiceIpCmd = self.cmd.readXml('getServiceIp', self.backInfoPath)
        getRemoteServiceIp = self.ssh.connSsh(self.host, getRemoteServiceIpCmd)
        if getRemoteServiceIp[0] <> 0:
            ret = "errcode=" + str(getRemoteServiceIp[0]) + ";" + "errmsg=" + str(getRemoteServiceIp[1])
        else:
            ret = getRemoteServiceIp[2]
            remoteServiceIp = ret.strip()
            self.ssh.uploadFiles(remoteServiceIp, self.local_dir, self.remote_dir)
            killUaoThreadCmd = self.cmd.readXml('killUaoThread', self.backInfoPath)
            killUaoThread = self.ssh.connSsh(remoteServiceIp, killUaoThreadCmd)
            print killUaoThread[2]
            exceIneUaoCmd = self.cmd.readXml('exceIneUao', self.backInfoPath)
            exceIneUao = self.ssh.connSsh(remoteServiceIp, exceIneUaoCmd)
            if exceIneUao[0] <> 0:
                ret1 = "errcode=" + str(exceIneUao[0]) + ";" + "errmsg=" + str(exceIneUao[1])
            else:
                ret1 = exceIneUao[2]
        print ret, ret1
        print inMaxNo
        print seqNo

    #个人
    def test_Person_OpenCount(self):
        f1 = '../Results/personInput.json'
        f2 = '../Results/personOutput.json'
        self.x2j.personInfo(f1)
        findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
        sSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'cfmmc\''
        genMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'GEN_MAX_NO\''
        rSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'N\' '
        inMaxNo = self.getValue(findinMaxNosql)
        genMaxNo = self.getValue(genMaxNosql)
        sSeqNo = self.getValue(sSeqNosql)
        rSeqNo = self.getValue(rSeqNosql)
        analysisSendsql = 'select * from t_ineSeqProcess t  where t.sender = \'cfmmc\' and t.seqno >='+inMaxNo
        print analysisSendsql
        print inMaxNo, genMaxNo, sSeqNo, rSeqNo
        print 'Do sth .....'
        while True:
            while int(sSeqNo) == int(inMaxNo):
                print 'put t_ineSeqProcess data into json file'
                self.o2j.personRes(analysisSendsql, f2)
                print 'compare outputfile with input file'
                self.com.compareFiles(f1, f2)
                print 'ananlysis t_ineSeqProcess with xml'
                while int(genMaxNo) == int(rSeqNo):
                    print 'ananlysis result '
                    break
                break
            break






u = uao()
#u.uploadFiles()
# u.analysisRes()
#u.test_reStartUaoJob()
#u.test_uploadXmlFiles()
#print u.getValue('select * from t_inesetting t where t.SETTINGVALUE = \'1\'')
u.test_Person_OpenCount()
# jsonData = u.getJson('select * from t_inesetting t')
# print jsonData
# f = open(r'getuidata.txt', 'w+')
# f.write(str(jsonData))
# f.close()