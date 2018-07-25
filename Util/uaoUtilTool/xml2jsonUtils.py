# -*- coding: utf-8 -*-
'''
Created on 2018-06-04

@author: xu.ren
'''
import json
import xml.dom.minidom
import os


class xml2jsonUtils(object):

    def personInfo(self, local_dir, filePath):
        for f in os.listdir(local_dir):
            if f[-3:] == 'xml':
                inputfile = local_dir + f
                #DOMTree = xml.dom.minidom.parse('../a.xml')
                DOMTree = xml.dom.minidom.parse(inputfile)
                collection = DOMTree.documentElement
                packages = collection.getElementsByTagName('package')
                data = []
                for package in packages:
                    result = {}
                    seqno = package.getAttribute('seqno')
                    process = package.getElementsByTagName('process')[0]
                    processid = process.getAttribute('processid')
                    processstatus = process.getAttribute('processstatus')
                    processdate = process.getAttribute('processdate')
                    processtime = process.getAttribute('processtime')
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
                    f = open(filePath, 'w+')
                    f.write(str(jsonData))
                    f.close()
                print 'person xml2json done !!!'

    def organInfo(self, local_dir, filePath):
        for f in os.listdir(local_dir):
            if f[-3:] == 'xml':
                inputfile = local_dir + f
                #DOMTree = xml.dom.minidom.parse('../../Data/organAccount/cfmmc_N_20180620_00000002.xml')
                DOMTree = xml.dom.minidom.parse(inputfile)
                collection = DOMTree.documentElement
                packages = collection.getElementsByTagName('package')
                data = []
                for package in packages:
                    result = {}
                    seqno = package.getAttribute('seqno')
                    process = package.getElementsByTagName('process')[0]
                    processid = process.getAttribute('processid')
                    processstatus = process.getAttribute('processstatus')
                    processdate = process.getAttribute('processdate')
                    processtime = process.getAttribute('processtime')
                    processtype = process.getAttribute('processtype')
                    businesstype = process.getAttribute('businesstype')
                    organ_info = package.getElementsByTagName('organ_info')[0]
                    futuresid = organ_info.getAttribute('futuresid')
                    clienttype = organ_info.getAttribute('clienttype')
                    clientregion = organ_info.getAttribute('clientregion')
                    foreignclientmode = organ_info.getAttribute('foreignclientmode')
                    exchangeid = organ_info.getAttribute('exchangeid')
                    companyid = organ_info.getAttribute('companyid')
                    excompanyid = organ_info.getAttribute('excompanyid')
                    exclientidtype = organ_info.getAttribute('exclientidtype')
                    idtype = organ_info.getAttribute('idtype')
                    nocid = organ_info.getAttribute('nocid')
                    compclientid = organ_info.getAttribute('compclientid')
                    registry_addr_country = organ_info.getAttribute('registry_addr_country')

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
                    result['exchangeid'] = exchangeid
                    result['companyid'] = companyid
                    result['excompanyid'] = excompanyid
                    result['exclientidtype'] = exclientidtype
                    result['idtype'] = idtype
                    result['nocid'] = nocid
                    result['compclientid'] = compclientid
                    result['registry_addr_country'] = registry_addr_country

                    data.append(result)
                    jsonData = json.dumps(data, sort_keys=True, indent=2)
                    f = open(filePath, 'w+')
                    f.write(str(jsonData))
                    f.close()
                print 'organ xml2json done !!!'

    def specialorganInfo(self, local_dir, filePath):
        for f in os.listdir(local_dir):
            if f[-3:] == 'xml':
                inputfile = local_dir + f
                DOMTree = xml.dom.minidom.parse(inputfile)
                collection = DOMTree.documentElement
                packages = collection.getElementsByTagName('package')
                data = []
                for package in packages:
                    result = {}
                    seqno = package.getAttribute('seqno')
                    process = package.getElementsByTagName('process')[0]
                    processid = process.getAttribute('processid')
                    processstatus = process.getAttribute('processstatus')
                    processdate = process.getAttribute('processdate')
                    processtime = process.getAttribute('processtime')
                    processtype = process.getAttribute('processtype')
                    businesstype = process.getAttribute('businesstype')
                    specialorgan_info = package.getElementsByTagName('specialorgan_info')[0]
                    futuresid = specialorgan_info.getAttribute('futuresid')
                    clienttype = specialorgan_info.getAttribute('clienttype')
                    exchangeid = specialorgan_info.getAttribute('exchangeid')
                    companyid = specialorgan_info.getAttribute('companyid')
                    excompanyid = specialorgan_info.getAttribute('excompanyid')
                    exclientidtype = specialorgan_info.getAttribute('exclientidtype')
                    nocid = specialorgan_info.getAttribute('nocid')
                    licenseno = specialorgan_info.getAttribute('licenseno')
                    organtype = specialorgan_info.getAttribute('organtype')
                    compclientid = specialorgan_info.getAttribute('compclientid')
                    registry_addr_country = specialorgan_info.getAttribute('registry_addr_country')


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
                    result['exchangeid'] = exchangeid
                    result['companyid'] = companyid
                    result['excompanyid'] = excompanyid
                    result['exclientidtype'] = exclientidtype
                    result['nocid'] = nocid
                    result['licenseno'] = licenseno
                    result['organtype'] = organtype
                    result['compclientid'] = compclientid
                    result['registry_addr_country'] = registry_addr_country

                    data.append(result)
                    jsonData = json.dumps(data, sort_keys=True, indent=2)
                    f = open(filePath, 'w+')
                    f.write(str(jsonData))
                    f.close()
                print 'specialorgan xml2json done !!!'

    def assetInfo(self, local_dir, filePath):
        for f in os.listdir(local_dir):
            if f[-3:] == 'xml':
                inputfile = local_dir + f
                DOMTree = xml.dom.minidom.parse(inputfile)
                collection = DOMTree.documentElement
                packages = collection.getElementsByTagName('package')
                data = []
                for package in packages:
                    result = {}
                    seqno = package.getAttribute('seqno')
                    process = package.getElementsByTagName('process')[0]
                    processid = process.getAttribute('processid')
                    processstatus = process.getAttribute('processstatus')
                    processdate = process.getAttribute('processdate')
                    processtime = process.getAttribute('processtime')
                    processtype = process.getAttribute('processtype')
                    businesstype = process.getAttribute('businesstype')
                    asset_info = package.getElementsByTagName('asset_info')[0]
                    clientregion = asset_info.getAttribute('clientregion')
                    futuresid = asset_info.getAttribute('futuresid')
                    clienttype = asset_info.getAttribute('clienttype')
                    exchangeid = asset_info.getAttribute('exchangeid')
                    companyid = asset_info.getAttribute('companyid')
                    excompanyid = asset_info.getAttribute('excompanyid')
                    exclientidtype = asset_info.getAttribute('exclientidtype')
                    nationality = asset_info.getAttribute('nationality')
                    idtype = asset_info.getAttribute('idtype')
                    id_original = asset_info.getAttribute('id_original')
                    nocid = asset_info.getAttribute('nocid')
                    licenseno = asset_info.getAttribute('licenseno')
                    organtype = asset_info.getAttribute('organtype')

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
                    result['exchangeid'] = exchangeid
                    result['companyid'] = companyid
                    result['excompanyid'] = excompanyid
                    result['exclientidtype'] = exclientidtype
                    result['nocid'] = nocid
                    result['licenseno'] = licenseno
                    result['organtype'] = organtype
                    result['clientregion'] = clientregion
                    result['nationality'] = nationality
                    result['idtype'] = idtype
                    result['id_original'] = id_original

                    data.append(result)
                    jsonData = json.dumps(data, sort_keys=True, indent=2)
                    f = open(filePath, 'w+')
                    f.write(str(jsonData))
                    f.close()
                print 'asset xml2json done !!!'
# a = xml2jsonUtils()
# f1 = '../../Data/organAccount/cfmmc_N_20180620_00000002.xml'
# f2 = 'organInput.json'
#
# local_dir = 'D:/testPlam/Taffy-master/Data/organAccount/'
# # for f in os.listdir(local_dir):
# #     if f[-3:] == 'xml':
# #         print f
#
# a.organInfo(local_dir, f2)


