#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class seleniumAccountRecordUtils(object):

    def review(self, type, id):
        time.sleep(30)
        flag = False
        driver = webdriver.Ie()
        driver.get('http://172.24.118.9:7003/')
        #driver.get("javascript:document.getElementById('overridelink').click();")
        #driver.get("javascript:document.getElementById('overridelink').click();")
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector('#formUserName').send_keys('sun.wei')
        driver.find_element_by_css_selector('#formPassword').clear()
        driver.find_element_by_css_selector('#formPassword').send_keys('111111')
        driver.find_element_by_css_selector('#userInfoForm').submit()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[text()='投资者信息管理']").click()
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_xpath("//*[text()='投资者开户申请备案']").click()
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.switch_to_frame('mainframe')
        if type == 'person':
            driver.find_element_by_xpath("//label[text()='个人']").click()
            driver.implicitly_wait(10)
            while True:
                driver.find_element_by_xpath("//*[text()='查询']").click()
                time.sleep(10)
                list = driver.find_element_by_class_name('TextCell')
                alllist = []
                for l in list:
                    v = l.get_attribute('title')
                    alllist.append(v)
                print alllist
                if set(id).issubset(set(alllist)):
                    print 'ok'
                    for i in id:
                        driver.find_element_by_xpath("//td/div[@title='"+ i +"']").click()
                        time.sleep(2)
                        for j in driver.find_elements_by_xpath("//tbody/tr[@class='CurrentRow']/td[1]/div/input[@type='checkbox']"):
                            if j.is_displayed():
                                j.click()
                    time.sleep(2)
                    flag = True
                if flag:
                    break
            driver.find_element_by_xpath("//button[@id='buttonIndiSelectAudit']").click()
            time.sleep(2)
        elif type == 'organ':
            driver.find_element_by_xpath("//label[text()='一般单位']").click()
            driver.implicitly_wait(10)
            while True:
                driver.find_element_by_xpath("//*[text()='查询']").click()
                time.sleep(10)
                list = driver.find_elements_by_class_name('TextCell')
                alllist = []
                for l in list:
                    v = l.get_attribute('title')
                    alllist.append(v)
                print 'not find processingno'
                if set(id).issubset(set(alllist)):
                    print 'ok'
                    for i in id:
                        driver.find_element_by_xpath("//td/div[@title='"+ i +"']").click()
                        time.sleep(2)
                        for j in driver.find_elements_by_xpath("//tbody/tr[@class='CurrentRow']/td[1]/div/input[@type='checkbox']"):
                            if j.is_displayed():
                                j.click()
                    time.sleep(2)
                    flag = True
                if flag:
                    break
            driver.find_element_by_xpath("//button[@id='buttonCorpSelectAudit']").click()
            time.sleep(2)
        elif type == 'specialorgan':
            driver.find_element_by_xpath("//label[text()='特殊单位']").click()
            driver.implicitly_wait(10)
            while True:
                driver.find_element_by_xpath("//*[text()='查询']").click()
                time.sleep(10)
                list = driver.find_element_by_class_name('TextCell')
                alllist = []
                for l in list:
                    v = l.get_attribute('title')
                    alllist.append(v)
                print alllist
                if set(id).issubset(set(alllist)):
                    print 'ok'
                    for i in id:
                        driver.find_element_by_xpath("//td/div[@title='"+ i +"']").click()
                        time.sleep(2)
                        for j in driver.find_elements_by_xpath("//tbody/tr[@class='CurrentRow']/td[1]/div/input[@type='checkbox']"):
                            if j.is_displayed():
                                j.click()
                    time.sleep(2)
                    flag = True
                if flag:
                    break

            driver.find_element_by_xpath("//button[@id='buttonSpecCorpAllAudit']").click()
            time.sleep(2)
        elif type == 'asset':
            driver.find_element_by_xpath("//label[text()='资管客户']").click()
            driver.implicitly_wait(10)
            while True:
                driver.find_element_by_xpath("//*[text()='查询']").click()
                time.sleep(10)
                list = driver.find_element_by_class_name('TextCell')
                alllist = []
                for l in list:
                    v = l.get_attribute('title')
                    alllist.append(v)
                print alllist
                if set(id).issubset(set(alllist)):
                    print 'ok'
                    for i in id:
                        driver.find_element_by_xpath("//td/div[@title='"+ i +"']").click()
                        time.sleep(2)
                        for j in driver.find_elements_by_xpath("//tbody/tr[@class='CurrentRow']/td[1]/div/input[@type='checkbox']"):
                            if j.is_displayed():
                                j.click()
                    time.sleep(2)
                    flag = True
                if flag:
                    break

            driver.find_element_by_xpath("//button[@id='buttonAssetSelectAudit']").click()
            time.sleep(2)

        driver.find_element_by_xpath("//textarea[@name='ReplyRemark']").send_keys("agree")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//button[@id='buttonAdopt']").click()
        time.sleep(3)
        #driver.refresh()

#a = seleniumAccountRecordUtils()
# alllist = ['a', 'b', 'c', 'd']
# id = ['c', 'e']
# if set(id).issubset(set(alllist)):
#     print 'ok'
#a.review('corporation', id)
