# -*- coding: utf-8 -*-
'''
Created on 2018-05-22

@author: xu.ren
'''

from Util import *

class uao(object):
    backInfoPath = 'D:/testPlam/Taffy-master/config/backInfo.xml'
    local_dir = 'D:/testPlam/Taffy-master/config/openAccountData/'
    remote_dir = '/home/uapp/zzz/'
    host = '172.24.118.9'
    cmd = xmlUtils()
    ssh = sshUtils()
    x2j = xml2jsonUtils()
    o2j = oracle2jsonUtils()
    com = compareFiles()
    orcl = orclUtils()

    def getValue(self, sql):
        data = self.orcl.connOrcl(sql)
        for row in data[2]:
            for r in row:
                value = r
                #print value
        return value


    def analysisTestResult(self, inseqno, respseqno):
        f1 = '../../Results/personInput.json'
        f2 = '../../Results/personOutput.json'
        self.x2j.personInfo(f1)
        findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
        sSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'cfmmc\''
        genMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'GEN_MAX_NO\''
        rSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'N\' '
        analysisSendsql = 'select * from t_ineSeqProcess t  where t.sender = \'cfmmc\' and t.seqno >'+inseqno+' order by t.seqno desc'
        analysisRessql = 'select  t.seqno,t.exreturncode,t.exreturnmsg  from t_ineSeqProcess t  where t.sender = \'N\' and t.seqno ='+respseqno+' order by t.seqno desc'
        print 'Do sth .....'
        flag = False
        while True:
            inMaxNo = self.getValue(findinMaxNosql)
            sSeqNo = self.getValue(sSeqNosql)
            genMaxNo = self.getValue(genMaxNosql)
            if int(sSeqNo) == int(inMaxNo):
                flag = True
                num = int(inMaxNo) - int(inseqno)
                rSeqNo = int(respseqno) + num
                print rSeqNo
                print genMaxNo
                print 'put SeqProcess data into json file'
                self.o2j.personData(analysisSendsql, f2)
                print 'compare outputfile with inputfile'
                self.com.compareFile(f1, f2)
                print 'ananlysis table SeqProcess response'
                while 1:
                    if int(genMaxNo) == int(rSeqNo):
                        analysisRes = self.orcl.connOrcl(analysisRessql)[2]
                        for i in analysisRes:
                            if i[1] <> 0:
                                print 'seqno = '+str(i[0])+' operate filed and errmsg: ' + str(i[2])
                            else:
                                print 'seqno = '+str(i[0])+' operate success and sucmsg: ' + str(i[2])
                        print 'ananlysis result end'
                        break
                    else:
                        genMaxNo = self.getValue(genMaxNosql)
            if flag:
                break

    #重启uao job
    def test_reStartUaoJob(self):
        restartUaoCmd = self.cmd.readXml('restartUao', self.backInfoPath)
        restart = self.ssh.connSsh(self.host, restartUaoCmd)
        if restart[0] <> 0:
            ret = "errcode=" + str(restart[0]) + ";" + "errmsg=" + str(restart[1])
        else:
            ret = restart[2]
        print ret

    #上传xml文件，执行uao
    def executeUao(self, local_dir):
        getRemoteServiceIpCmd = self.cmd.readXml('getServiceIp', self.backInfoPath)
        getRemoteServiceIp = self.ssh.connSsh(self.host, getRemoteServiceIpCmd)
        if getRemoteServiceIp[0] <> 0:
            ret = "errcode=" + str(getRemoteServiceIp[0]) + ";" + "errmsg=" + str(getRemoteServiceIp[1])
        else:
            ret = getRemoteServiceIp[2]
            remoteServiceIp = ret.strip()
            self.ssh.uploadFiles(remoteServiceIp, local_dir, self.remote_dir)
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



    #个人
    def test_Person_OpenCount(self):
        local_dir = 'D:/testPlam/Taffy-master/config/openAccountData/'
        #获取当前的seqno
        findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
        genMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'GEN_MAX_NO\''
        inseqno = self.getValue(findinMaxNosql)
        respseqno = self.getValue(genMaxNosql)
        print inseqno, respseqno
        #执行uao job
        uploadFiles = self.executeUao(local_dir)
        #结果对比
        self.analysisTestResult(inseqno, respseqno)





    # def test_Person_OpenCount1(self):
    #     f1 = '../../Results/personInput.json'
    #     f2 = '../../Results/personOutput.json'
    #     self.x2j.personInfo(f1)
    #     findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
    #     sSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'cfmmc\''
    #     genMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'GEN_MAX_NO\''
    #     rSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'N\' '
    #     inMaxNo = self.getValue(findinMaxNosql)
    #     genMaxNo = self.getValue(genMaxNosql)
    #     sSeqNo = self.getValue(sSeqNosql)
    #     rSeqNo = self.getValue(rSeqNosql)
    #     analysisSendsql = 'select * from t_ineSeqProcess t  where t.sender = \'cfmmc\' and t.seqno >='+inMaxNo+' order by t.seqno desc'
    #     analysisRessql = 'select  t.seqno,t.exreturncode,t.exreturnmsg  from t_ineSeqProcess t  where t.sender = \'N\' and t.seqno >='+genMaxNo+' order by t.seqno desc'
    #     analysisRes = self.orcl.connOrcl(analysisRessql)[2]
    #     print analysisSendsql
    #     print inMaxNo, genMaxNo, sSeqNo, rSeqNo
    #     print 'Do sth .....'
    #     while True:
    #         print 'gggggggggggggggggoooooooooo'
    #         while int(sSeqNo) == int(inMaxNo):
    #             print 'put SeqProcess data into json file'
    #             self.o2j.personData(analysisSendsql, f2)
    #             print 'compare outputfile with input file'
    #             self.com.compareFile(f1, f2)
    #             print 'ananlysis t_ineSeqProcess with xml'
    #             while int(genMaxNo) == int(rSeqNo):
    #                 for i in analysisRes:
    #                     if i[1] <> 0:
    #                         print 'seqno = '+str(i[0])+' operate filed and errmsg: ' + str(i[2])
    #                     else:
    #                         print 'seqno = '+str(i[0])+' operate success and sucmsg: ' + str(i[2])
    #                 print 'ananlysis result end'
    #                 break
    #             break
    #         break
    #




#u = uao()
#u.test_Person_OpenCount()
#u.uploadFiles()
# u.analysisRes()
#u.test_reStartUaoJob()
#u.test_uploadXmlFiles()
#print u.getValue('select * from t_inesetting t where t.SETTINGVALUE = \'1\'')
#u.test_Person_OpenCount()
# jsonData = u.getJson('select * from t_inesetting t')
# print jsonData
# f = open(r'getuidata.txt', 'w+')
# f.write(str(jsonData))
# f.close()