# -*- coding: utf-8 -*-
'''
Created on 2018-06-04

@author: xu.ren
'''
import json
import cx_Oracle
import os
from Util.uaoUtilTool import orclUtils

class oracle2json(object):

    def personRes(self, sql):
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
            f = open(r'../../Results/personOutput.json', 'w+')
            f.write(str(jsonData))
            f.close()
        print 'Person oracle2json done !!!'

