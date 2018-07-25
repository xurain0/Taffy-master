# coding=utf-8

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from Util import *
from selenium import webdriver
import time

selenium_yml = '/config/selenium.yml'

class test_login(object):
    def __init__(self):
        pass
    @staticmethod
    def login(self):
        time.sleep(1)
        driver = webdriver.Firefox()
        driver.get("http:baidu.com")
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys(u'你好')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        driver.quit()
    def test_login(self):
        # 测试用例：密码错误，登陆失败
        test_login.login(self)
# if __name__ == "__main__":
#     login = test_login()
#     login.login()