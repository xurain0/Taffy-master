# -*- coding: utf-8 -*-
'''
Created on 2018-06-04

@author: xu.ren
'''
import json
import xml.dom.minidom

class xml2json(object):
    def personInfo(self):
        DOMTree = xml.dom.minidom.parse('a.xml')
        collection = DOMTree.documentElement
        packages = collection.getElementsByTagName('package')
        data = []
        for package in packages:
            result = {}
            seqno = package.getAttribute('seqno')
            process = package.getElementsByTagName('process')[0]
            processid = process.getAttribute('processid')
            processstatus = process.getAttribute('processstatus')
            processdate  = process.getAttribute('processdate')
            processtime  = process.getAttribute('processtime')
            processtype = process.getAttribute('processtype')
            businesstype = process.getAttribute('businesstype')
            person_info = package.getElementsByTagName('person_info')[0]
            futuresid = person_info.getAttribute('futuresid')
            clienttype = person_info.getAttribute('clienttype')
            clientregion = person_info.getAttribute('clientregion')
            foreignclientmode = person_info.getAttribute('foreignclientmode')
            idtype= person_info.getAttribute('idtype')
            id_original = person_info.getAttribute('id_original')
            id_transformed = person_info.getAttribute('id_transformed')
            nationality= person_info.getAttribute('nationality')
            result['sender'] = 'cfmmc'
            result['receiver'] = 'N'
            result['seqno'] = seqno
            result['processid'] = processid
            result['processtype'] = processtype
            result['businesstype'] = businesstype
            result['processstatus'] = processstatus
            result['processdate'] = processdate
            result['processtime'] = processtime
            result['futuresid'] = futuresid
            result['clienttype'] = clienttype
            result['clientregion'] = clientregion
            result['foreignclientmode'] = foreignclientmode
            result['idtype'] = idtype
            result['id_original'] = id_original
            result['id_transformed'] = id_transformed
            result['nationality'] = nationality
            data.append(result)
            jsonData = json.dumps(data, sort_keys=True, indent=2)
            f = open(r'../../Results/personInput.json', 'w+')
            f.write(str(jsonData))
            f.close()
        print 'person xml2json done !!!'