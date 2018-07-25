# -*- coding: utf-8 -*-
'''
Created on 2018-05-22
@author: xu.ren
'''

from xml.dom import minidom

class xmlUtils(object):

    def readXml(self, propertyID, path):
        try:
            s = ""

            doc1 = minidom.parse(path)
            root1 = doc1.documentElement
            nodes1 = root1.getElementsByTagName("property")

            for n in nodes1:
                if propertyID==n.getAttribute("id"):
                    s=n.getAttribute("s")

        except Exception, e:
            errmsg = e.args[0]
            code = -1
            print "errcode=" + str(code)+";"+"errmsg=" + str(errmsg)+";"
        return s
