# -*- coding: utf-8 -*-
'''
Created on 2018-06-04

@author: xu.ren
'''
import json
import cx_Oracle
import os
from Util.uaoUtilTool.orclUtils import orclUtils

class oracle2jsonUtils(object):

    def replace(self, filePath):
        with open(filePath, "r") as f:
            lines = f.readlines()
        #把文件中null字段替换为""
        with open(filePath, "w") as f_w:
            for line in lines:
                if 'null' in line:
                 #替换
                    line = line.replace('null', '\"\"')
                f_w.write(line)
        f.close()

    def personData(self, sql, filePath):
        ora = orclUtils()
        data = ora.connOrcl(sql)
        jd = []
        for row in data[2]:
            result = {}
            result['sender'] = row[1]
            result['receiver'] = row[2]
            result['seqno'] = str(row[4])
            result['processid'] = row[5]
            result['processtype'] = row[6].strip()
            result['businesstype'] = row[7]
            result['processstatus'] = str(row[8])
            result['processdate'] = row[9]
            result['processtime'] = row[10]
            result['futuresid'] = row[11]
            result['clienttype'] = row[12]
            result['clientregion'] = row[13]
            result['foreignclientmode'] = row[14].strip()
            result['idtype'] = row[15].strip()
            result['id_original'] = row[16]
            result['id_transformed'] = row[17]
            result['nationality'] = row[18]

            jd.append(result)
            jsonData = json.dumps(jd, sort_keys=True, indent=2)
            f = open(filePath, 'w+')
            f.write(str(jsonData))
            self.replace(filePath)
            f.close()
        print 'Person oracle2json done !!!'


    def organData(self, sql, filePath):
        ora = orclUtils()
        data = ora.connOrcl(sql)
        jd = []
        for row in data[2]:
            result = {}
            result['sender'] = row[1]
            result['receiver'] = row[2]
            result['seqno'] = str(row[4])
            result['processid'] = row[5]
            result['processtype'] = row[6].strip()
            result['businesstype'] = row[7]
            result['processstatus'] = str(row[8])
            result['processdate'] = row[9]
            result['processtime'] = row[10]
            result['futuresid'] = row[11]
            result['clienttype'] = row[12]
            result['clientregion'] = row[13]
            result['foreignclientmode'] = row[14].strip()
            result['idtype'] = row[15].strip()
            result['exchangeid'] = row[52]
            result['companyid'] = row[50]
            result['excompanyid'] = row[55]
            result['exclientidtype'] = row[56]
            result['nocid'] = row[47]
            result['compclientid'] = row[51]
            result['registry_addr_country'] = row[41]

            jd.append(result)
            jsonData = json.dumps(jd, sort_keys=True, indent=2)
            f = open(filePath, 'w+')
            f.write(str(jsonData))
            f.close()
            self.replace(filePath)
        print 'organ oracle2json done !!!'

    def specialorganData(self, sql, filePath):
        ora = orclUtils()
        data = ora.connOrcl(sql)
        jd = []
        print 'specialorgan oracle2json begin !!!'
        for row in data[2]:
            result = {}
            result['sender'] = row[1]
            result['receiver'] = row[2]
            result['seqno'] = str(row[4])
            result['processid'] = row[5]
            result['processtype'] = row[6].strip()
            result['businesstype'] = row[7]
            result['processstatus'] = str(row[8])
            result['processdate'] = row[9]
            result['processtime'] = row[10]
            result['futuresid'] = row[11]
            result['clienttype'] = row[12]
            result['exchangeid'] = row[52]
            result['companyid'] = row[50]
            result['excompanyid'] = row[55]
            result['exclientidtype'] = row[56]
            result['nocid'] = row[47]
            result['licenseno'] = row[60]
            result['organtype'] = row[58]
            result['compclientid'] = row[51]
            result['registry_addr_country'] = row[41]

            jd.append(result)
            jsonData = json.dumps(jd, sort_keys=True, indent=2)
            f = open(filePath, 'w+')
            f.write(str(jsonData))
            self.replace(filePath)
            f.close()
        print 'specialorgan oracle2json done !!!'

    def assetData(self, sql, filePath):
        ora = orclUtils()
        data = ora.connOrcl(sql)
        jd = []
        for row in data[2]:
            result = {}
            result['sender'] = row[1]
            result['receiver'] = row[2]
            result['seqno'] = str(row[4])
            result['processid'] = row[5]
            result['processtype'] = row[6].strip()
            result['businesstype'] = row[7]
            result['processstatus'] = str(row[8])
            result['processdate'] = row[9]
            result['processtime'] = row[10]
            result['futuresid'] = row[11]
            result['clienttype'] = row[12]
            result['exchangeid'] = row[52]
            result['companyid'] = row[50]
            result['excompanyid'] = row[55]
            result['exclientidtype'] = row[56]
            result['nocid'] = row[47]
            result['organtype'] = row[58]
            result['licenseno'] = row[60]
            result['clientregion'] = row[13]
            result['nationality'] = row[18]
            result['idtype'] = row[15].strip()
            result['id_original'] = row[16]

            jd.append(result)
            jsonData = json.dumps(jd, sort_keys=True, indent=2)
            f = open(filePath, 'w+')
            f.write(str(jsonData))
            self.replace(filePath)
            f.close()
        print 'asset oracle2json done !!!'

# a = oracle2jsonUtils()
# analysisSendsql = 'select * from t_ineSeqProcess t  where t.sender = \'cfmmc\' and t.seqno >120 '
# f = 'specialorganOutput.json'
# a.specialorganData(analysisSendsql, f)
