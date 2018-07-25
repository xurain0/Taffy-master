# -*- coding: utf-8 -*-
'''
Created on 2018-06-05

@author: xu.ren
'''

import difflib
import sys
class compareFilesUtils(object):

    def compareFile(self, f1, f2):
        inputFile = open(f1)
        outputFile = open(f2)

        count = 0
        dif = []
        for a in inputFile:
          b = outputFile.readline()
          count += 1
          if a != b:
              dif.append(count)
        if dif == []:
             print('两个json文件一样！！！')
        else:
             print('有%d处不同'% len(dif))
             for each in dif:
                  print('%d行不一样'% each)
        #create diff html
        text1_lines = open(f1, 'U').readlines()
        text2_lines = open(f2, 'U').readlines()
        d = difflib.HtmlDiff()
        dm = d.make_file(text1_lines, text2_lines)
        with open(r'../../Results/IOdiff.html', 'w') as resultfile:
                resultfile.write(dm)
        inputFile.close()
        outputFile.close()