# coding=utf-8

import sys
import os
import time
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from Util import *

class test_openAccount(object):
    def __init__(self):
        pass

    @staticmethod
    def yamlLoad():
        CONFIG_FILE = '../config/test.yaml'
        with open(CONFIG_FILE, 'r') as f:
            temp = yaml.load(f.read())
            return temp
    @staticmethod
    def common(self, inFile, xmlPath, outFile):
        analyXml = analysisXml()
        tree = analyXml.read_xml(inFile)
        param =test_openAccount.yamlLoad()
        exchangeid = param["exchangeid"]
        companyid = str(param["client"]).zfill(4)
        processdate = str(param["processdate"])
        exclientidtype = str(param["exclientidtype"])
        seqno = "200"
        date = str(processdate)[0:4]+str(processdate)[5:7]+str(processdate)[8:10]
        processid = companyid + "-A-" + date + "-000003"
        #test_xml.common(inFile, exchangeid, processid, processdate, outFile)
        nodesA = analyXml.find_nodes(tree, "package_list")
        analyXml.change_node_properties(nodesA, {"to": exchangeid})
        nodesB = analyXml.find_nodes(tree, "package_list/package")
        analyXml.change_node_properties(nodesB, {"seqno": seqno})
        nodesC = analyXml.find_nodes(tree, "package_list/package/process")
        analyXml.change_node_properties(nodesC, {"processid": processid})
        analyXml.change_node_properties(nodesC, {"processdate": processdate})
        nodesD = analyXml.find_nodes(tree, xmlPath)
        analyXml.change_node_properties(nodesD, {"exchangeid": exchangeid})
        analyXml.change_node_properties(nodesD, {"companyid": companyid})
        analyXml.change_node_properties(nodesD, {"excompanyid": companyid})
        analyXml.change_node_properties(nodesD, {"exclientidtype": exclientidtype})
        path = "../config/openAccountData/cfmmc_" + exchangeid +"_" + date + "_" + outFile
        analyXml.write_xml(tree, path)

    #个人
    def test_Person_OpenCount(self):
        inFile = "../config/Data/cfmmc_S_date_00000001.xml"
        xmlPath = "package_list/package/process/person_info"
        outFile = "00000001.xml"
        test_openAccount.common(self, inFile, xmlPath, outFile)

    #一般单位
    def test_Organ_OpenAccount(self):
        inFile = "../config/Data/cfmmc_S_date_00000002.xml"
        xmlPath = "package_list/package/process/organ_info"
        outFile = "00000002.xml"
        test_openAccount.common(self, inFile, xmlPath, outFile)

    #特殊单位
    def test_SpecialOrgan_OpenAccount(self):
        inFile = "./config/Data/cfmmc_S_date_00000003.xml"
        xmlPath = "package_list/package/process/specialorgan_info"
        outFile = "00000003.xml"
        test_openAccount.common(self, inFile, xmlPath, outFile)

    #资管个人
    def test_Asset_OpenAccount(self):
        inFile = "./config/Data/cfmmc_S_date_00000004.xml"
        xmlPath = "package_list/package/process/asset_info"
        outFile = "00000004.xml"
        test_openAccount.common(self, inFile, xmlPath, outFile)
