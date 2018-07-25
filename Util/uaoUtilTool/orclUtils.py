# -*- coding: utf-8 -*-
'''
Created on 2018-5-21

@author: xu.ren
'''
import cx_Oracle
import os
import datetime

class orclUtils(object):
    username = 'party'
    password = 'oracle'
    hostname = '172.24.118.15:1521/tbdb'
    def connOrcl(self, sql):
        code = 0
        errmsg = ""
        status = ""
        conn = ""
        cr = ""
        r = ""
        try:
            conn = cx_Oracle.connect(self.username, self.password, self.hostname)
            cr = conn.cursor()
            cr.execute(sql)
            data = cr.fetchall()
            # for row in cr.fetchall():
            #     for r in row:
            #         status = r
            #         print status
            cr.close()
            conn.commit()
            conn.close()

        except cx_Oracle.Error, e:
            errmsg = e.args[0]
            code = -1

        return code, errmsg, data

#
# a = orclUtils()
# processingno = '1775900'
# processingnosql = 'select t.processingno from t_ineSeqProcess t  where t.sender = \'cfmmc\'  and t.seqno = 103'
# #operationsql = 'select * from party.t_operationlog t where t.logdesc like \'%ProcessingNo: '+processingno+'%\''
# b = a.getValue(processingnosql)
# c = a.connOrcl(processingnosql)
# print b
# print c[2]
# print str(c[2][0][0])
# id = ['1775890']
#
# d = datetime.datetime.now()
# date = d.year, d.month, d.day
# print '%s%s%s'%date
# f = str(datetime.date.today()).replace('-', '')
# print f