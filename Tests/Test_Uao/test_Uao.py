# -*- coding: utf-8 -*-
'''
Created on 2018-05-22

@author: xu.ren
'''

from Util import *
import time
import datetime


class test_Uao(object):
    backInfoPath = 'D:/testPlam/Taffy-master/config/backInfo.xml'
    #local_dir = 'D:/testPlam/Taffy-master/config/openAccountData/'
    remote_dir = '/home/uapp/services/uao_ineuao1/recv/'
    host = '172.24.118.9'
    cmd = xmlUtils()
    ssh = sshUtils()
    x2j = xml2jsonUtils()
    o2j = oracle2jsonUtils()
    compf = compareFilesUtils()
    orcl = orclUtils()
    accountRecord = seleniumAccountRecordUtils()

    def getValue(self, sql):
        result = []
        v = self.orcl.connOrcl(sql)
        for row in v[2]:
            for r in row:
                value = r
                result.append(str(value))
        return result

    def initialData(self):
        #findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
        #genMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'GEN_MAX_NO\''
        findinMaxNosql = self.cmd.readXml('findinMaxNosql', self.backInfoPath)
        genMaxNosql = self.cmd.readXml('genMaxNosql', self.backInfoPath)
        inseqno = self.getValue(findinMaxNosql)[0]
        respseqno = self.getValue(genMaxNosql)[0]
        print 'inseqno = ', inseqno, '    respseqno = ', respseqno
        return inseqno, respseqno

    #上传xml文件，执行uao
    def executeUao(self, local_dir):
        #获取当前日期，例如20180622
        date = str(datetime.date.today()).replace('-', '')
        #获取uao远程部署的服务地址
        getRemoteServiceIpCmd = self.cmd.readXml('getServiceIp', self.backInfoPath)
        getRemoteServiceIp = self.ssh.connSsh(self.host, getRemoteServiceIpCmd)
        if getRemoteServiceIp[0] <> 0:
            ret = "errcode=" + str(getRemoteServiceIp[0]) + ";" + "errmsg=" + str(getRemoteServiceIp[1])
        else:
            ret = getRemoteServiceIp[2]
            remoteServiceIp = ret.strip()
            print 'get uao remote service ip :', remoteServiceIp
            #上传xml文件到recv
            self.ssh.uploadFiles(remoteServiceIp, local_dir, self.remote_dir, date)
            killUaoThreadCmd = self.cmd.readXml('killUaoThread', self.backInfoPath)
            killUaoThread = self.ssh.connSsh(remoteServiceIp, killUaoThreadCmd)
            print killUaoThread[2]
            #exceIneUaoCmd = self.cmd.readXml('exceIneUao', self.backInfoPath)
            s = "source ~/.bash_profile ; /home/uapp/zzz/test.sh  " + date
            exceIneUao = self.ssh.connSsh(remoteServiceIp, s)
            if exceIneUao[0] <> 0:
                ret1 = "errcode=" + str(exceIneUao[0]) + ";" + "errmsg=" + str(exceIneUao[1])
            else:
                ret1 = exceIneUao[2]
        print ret, ret1


    def analysisTestResult(self, local_dir, inseqno, respseqno, type):
        #xml文件数据转成input.json，oralce中流水表数据转成output.json
        #统一开户业务流水表中直到seqno=配置文件seqno，对比这条流水与xml配置文件信息是否一致
        if type == 'person':
            f1 = '../../Results/personInput.json'
            print 'put xml data into personInput json file'
            self.x2j.personInfo(local_dir, f1)
        if type == 'organ':
            f1 = '../../Results/organInput.json'
            print 'put xml data into organInput json file'
            self.x2j.organInfo(local_dir, f1)
        if type == 'specialorgan':
            f1 = '../../Results/specialorganInput.json'
            print 'put xml data into specialorganInput json file'
            self.x2j.specialorganInfo(local_dir, f1)
        if type == 'asset':
            f1 = '../../Results/assetInput.json'
            print 'put xml data into assetInput json file'
            self.x2j.assetInfo(local_dir, f1)
        # findinMaxNosql = 'select t.settingvalue from t_inesetting t where t.settingkey = \'IN_MAX_NO\''
        # sSeqNosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'cfmmc\''
        findinMaxNosql = self.cmd.readXml('findinMaxNosql', self.backInfoPath)
        sSeqNosql = self.cmd.readXml('sSeqNosql', self.backInfoPath)
        analysisSendsql = 'select * from t_ineSeqProcess t  where t.sender = \'cfmmc\' and t.seqno >'+inseqno
        flag = False
        while True:
            inMaxNo = self.getValue(findinMaxNosql)[0]
            sSeqNo = self.getValue(sSeqNosql)[0]
            if int(sSeqNo) == int(inMaxNo):
                flag = True
                print 'put t_SeqProcess data into json file'
                if type == 'person':
                    f2 = '../../Results/personOutput.json'
                    self.o2j.personData(analysisSendsql, f2)
                if type == 'organ':
                    f2 = '../../Results/organOutput.json'
                    self.o2j.organData(analysisSendsql, f2)
                if type == 'specialorgan':
                    f2 = '../../Results/specialorganOutput.json'
                    self.o2j.specialorganData(analysisSendsql, f2)
                if type == 'asset':
                    f2 = '../../Results/assetOutput.json'
                    self.o2j.assetData(analysisSendsql, f2)
                print 'compare outputfile with inputfile'
                self.compf.compareFile(f1, f2)
            if flag:
                break

    def getResult(self, inseqno, respseqno, type):
        #clientregionsql=1,4境内客户不需要页面审核，境外需要页面审核
        #time.sleep(60)
        print 'ananlysis table SeqProcess response'
        start = time.clock()
        flag = False
        clientregionsql = 'select t.clientregion,t.processingno from t_ineSeqProcess t  where t.sender = \'cfmmc\'  and t.seqno > '+inseqno
        clientregion = self.orcl.connOrcl(clientregionsql)[2]
        print clientregion
        processingnolist = []
        count = 0
        length = len(clientregion)
        for c in clientregion:
            clientregionNo = int(c[0])
            processingno = str(c[1])
            #clientregionNo = 2,3 境外客户,找出境外客户的processingno，利用processingno在业务进行备案审核
            if clientregionNo == 2 or clientregionNo == 3:
                count = count + 1
                while True:
                    #查询t_operationlog，直到processingno这条记录处理完，去页面处理
                    operationsql = 'select * from party.t_operationlog t where t.logdesc like \'%ProcessingNo: '+processingno+'%\''
                    print operationsql
                    operationHasValue = self.orcl.connOrcl(operationsql)[2]
                    if operationHasValue != []:
                        processingnolist.append(str(processingno))
                        flag = True
                    print processingnolist
                    if flag:
                        break
            #clientregionNo = 1,4 境内客户
            elif clientregionNo == 1 or clientregionNo == 4:
                #length查出共有几条请求数据要处理，count查出几天数据是境外请求的。num为剩下的几条境内要处理的数据
                num = length - count
                if num > 0:
                    for n in range(1, num+1):
                        while True:
                            #查询t_ineSeqProcess返回给监控中心的数据是否处理。如果exreturncode=0表示处理成功。
                            end = time.clock()
                            if int(end - start) == 600:
                                print 'waiting for 10 min ,cant get result .Timeout!'
                                break
                            #初始的seqno加上递增的num
                            rSeqno = int(respseqno) + n
                            analysisRessql = 'select  t.seqno,t.exreturncode,t.exreturnmsg  from t_ineSeqProcess t  where t.sender = \'N\' and t.seqno ='+str(rSeqno)+' order by t.seqno desc'
                            maxSeqnosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'N\' '
                            maxRseqno = self.getValue(maxSeqnosql)[0]
                            if int(maxRseqno) >= int(rSeqno):
                                flag = True
                                analysisRes = self.orcl.connOrcl(analysisRessql)[2]
                                for i in analysisRes:
                                    if i[1] <> 0:
                                        print 'seqno = '+str(i[0])+' operate filed and errmsg: ' + str(i[2])
                                    else:
                                        print 'seqno = '+str(i[0])+' operate success and sucmsg: ' + str(i[2])
                                print 'ananlysis result end'
                            if flag:
                                break
        #存在境外客户的数据需要页面进行备案审核
        if count > 0:
            maxRsqnoplus = int(maxRseqno) + count + 1
            print 'selenium Account Record begin'
            print processingnolist
            test_Uao.accountRecord.review(type, processingnolist)
            print 'selenium Account Record end'
            for r in range(maxRseqno+1, maxRsqnoplus):
                analysisRessql = 'select  t.seqno,t.exreturncode,t.exreturnmsg  from t_ineSeqProcess t  where t.sender = \'N\' and t.seqno ='+str(r)+' order by t.seqno desc'
                analysisRes = self.orcl.connOrcl(analysisRessql)[2]
                for i in analysisRes:
                    if i[1] <> 0:
                        print 'seqno = '+str(i[0])+' operate filed and errmsg: ' + str(i[2])
                    else:
                        print 'seqno = '+str(i[0])+' operate success and sucmsg: ' + str(i[2])
                print 'ananlysis result end'


    #重启uao job
    def test_reStartUaoJob(self):
        restartUaoCmd = self.cmd.readXml('restartUao', self.backInfoPath)
        restart = self.ssh.connSsh(self.host, restartUaoCmd)
        if restart[0] <> 0:
            ret = "errcode=" + str(restart[0]) + ";" + "errmsg=" + str(restart[1])
        else:
            ret = restart[2]
        print ret


    #个人
    def test_Person_OpenAccount(self):
        type = 'person'
        local_dir = 'D:/testPlam/Taffy-master/Data/personAccount/'
        #获取当前的seqno
        inseqno = test_Uao().initialData()[0]
        respseqno = test_Uao().initialData()[1]
        #执行uao job
        test_Uao().executeUao(local_dir)
        #结果对比
        test_Uao().analysisTestResult(local_dir, inseqno, respseqno, type)
        #获取开户结果
        test_Uao().getResult(inseqno, respseqno, type)


    def test_Organ_OpenAccount(self):
        local_dir = 'D:/testPlam/Taffy-master/Data/organAccount/'
        type = 'organ'
        #获取当前的seqno
        inseqno = test_Uao().initialData()[0]
        respseqno = test_Uao().initialData()[1]
        #执行uao job
        test_Uao().executeUao(local_dir)
        #结果对比
        test_Uao().analysisTestResult(local_dir, inseqno, respseqno, type)
        #获取开户结果
        test_Uao().getResult(inseqno, respseqno, type)

    def test_Specialorgan_OpenAccount(self):
        type = 'specialorgan'
        local_dir = 'D:/testPlam/Taffy-master/Data/specialorganAccount/'
        #获取当前的seqno
        inseqno = test_Uao().initialData()[0]
        respseqno = test_Uao().initialData()[1]
        #执行uao job
        test_Uao().executeUao(local_dir)
        #结果对比
        test_Uao().analysisTestResult(local_dir, inseqno, respseqno, type)
        #获取开户结果
        test_Uao().getResult(inseqno, respseqno, type)

    def test_Asset_OpenAccount(self):
        type = 'asset'
        local_dir = 'D:/testPlam/Taffy-master/Data/assetAccount/'
        #获取当前的seqno
        inseqno = test_Uao().initialData()[0]
        respseqno = test_Uao().initialData()[1]
        #执行uao job
        test_Uao().executeUao(local_dir)
        #结果对比
        test_Uao().analysisTestResult(local_dir, inseqno, respseqno, type)
        #获取开户结果
        test_Uao().getResult(inseqno, respseqno, type)

u = test_Uao()
u.test_Organ_OpenAccount()
# local_dir = 'D:/testPlam/Taffy-master/Data/organAccount/'
# u.analysisTestResult(local_dir, '116', '105', 'organ')
#u.getResult('115', '102', 'organ')
# processingnosql = 'select t.processingno from t_ineSeqProcess t  where t.sender = \'cfmmc\'  and t.seqno = 118'
# clientregionsql = 'select t.clientregion, t.processingno from t_ineSeqProcess t  where t.sender = \'cfmmc\'  and t.seqno > 115'
# #processingno = u.getValue(processingnosql)
# clientregion = u.orcl.connOrcl(clientregionsql)[2]
#clientregion = u.getValue(clientregionsql)
# processingnolist = []
# count = 0
# for c in clientregion:
#     clientregionNo = int(c[0])
#     processingno = c[1]
#     if clientregionNo == 2 or clientregionNo == 3:
#         print 111111111
#         processingnolist.append(str(processingno))
#         count = count + 1
#         print count
#         print processingno
#     elif clientregionNo == 1 or clientregionNo == 4:
#         print count
#         print 222
#         print processingno
# print 'count = ', count
# print processingnolist
# print clientregion
# l = len(clientregion)
# # print l
# for i in range(0, 3+1):
#     print i


# rSeqnosql = 'select max(t.seqno) from t_ineSeqProcess t  where t.sender = \'N\' '
# maxRseqno = u.getValue(rSeqnosql)[0]
# print maxRseqno
# operationsql = 'select * from party.t_operationlog t where t.logdesc like \'%ProcessingNo: 1775902%\''
# #operationHasValue = u.getValue(operationsql)
# operationHasValue = u.orcl.connOrcl(operationsql)[2]
# print operationHasValue
# if operationHasValue != []:
#     print 'selenium Account Record begin'
# else:
#     print 3333333
#u.test_Organ_OpenAccount()
#
# ini = u.initialData()
# print ini
# print ini[0]
# print ini[1]


# local_dir = 'D:/testPlam/Taffy-master/config/openAccountData/'
# u.getResult('103','93')
#sql = 'select t.processingno from t_ineSeqProcess t  where t.sender = \'cfmmc\'  and t.seqno >= 90 order by t.seqno desc'
#print u.getValue(sql)

#print u.orcl.connOrcl(sql)[2]
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