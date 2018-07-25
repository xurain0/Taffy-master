# -*- coding: utf-8 -*-
'''
Created on 2018-06-05

@author: xu.ren
'''

import difflib
import sys
class compareFiles(object):

    def compareFiles(self, f1, f2):
        inputFile = open(f1)
        outputFile = open(f2)
        count = 0
        dif = []
        for a in inputFile:
          b = outputFile.readline()
          count += 1
          if a != b:
              dif.append(count)
        if dif == 0:
             print('两个文件一样！')
        else:
             print('有%d处不同'% len(dif))
             for each in dif:
                  print('%d行不一样'% each)
        #create diff html
        text1_lines = inputFile.read().splitlines()
        text2_lines = outputFile.read().splitlines()
        d = difflib.HtmlDiff()
        dm = d.make_file(text1_lines, text2_lines)
        with open(r'../Results/IOdiff.html', 'w') as resultfile:
                resultfile.write(dm)
        inputFile.close()
        outputFile.close()


# c = compareFiles()
# f1 = '../../Results/personInput.json'
# f2 = '../../Results/personOutput.json'
# c.compare(f1, f2)
# if e == 0:
#      print('两个文件一样！')
# else:
#      print('有%d处不同'% len(e))
#      for each in e:
#           print('%d行不一样'% each)
#
# import difflib
# import sys
#
# def readfile(filename):
#     try:
#         fileHandle = open(filename, 'r+')
#         text = fileHandle.read().splitlines()
#         fileHandle.close()
#         return text
#     except IOError as error:
#         print('Read file Error:' + str(error))
#         sys.exit()
f1 = '../../Results/personInput.json'
f2 = '../../Results/personOutput.json'
# text1_lines = readfile(f1)
# text2_lines = readfile(f2)
#
# d = difflib.HtmlDiff()
# dd = d.make_file(text1_lines, text2_lines)
# with open(r'../../Results/out.html', 'w') as resultfile:
#         resultfile.write(dd)
#
#
# a = open(f1, 'U').readlines()
# b = open(f2, 'U').readlines()
# diff = difflib.ndiff(a, b)
# d = difflib.HtmlDiff()
# dd = d.make_file(a, b)
# with open(r'../../Results/out.html', 'w') as resultfile:
#         resultfile.write(dd)
# print diff