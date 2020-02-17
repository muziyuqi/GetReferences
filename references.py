#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 注明：本方案参考 https://zhuanlan.zhihu.com/p/33385848 的方法，实现自动化获取参考文献。
#
# 使用方法：
# 本机需要部署：
# 1.安装python3
# 2.安装selenium包
# 3.以及浏览器对应的webdriver
# 4.articlename.txt中填写参考文献名称
# 5.运行程序
# chrome的webdriver下载地址【注意对应chrome版本号】：https://sites.google.com/a/chromium.org/chromedriver/downloads


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

with open('articlename.txt', 'rt', encoding='utf-8') as f:
    a_name = f.read()
referencename = a_name.split("\n")

outcome0 = []
exp=[]
for i in referencename:
    try:
        starturl = 'http://xueshu.baidu.com/s?wd='+i
        driver.get(starturl)
        driver.find_element_by_xpath("//i[@class='iconfont icon-cite']").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='sc_cit0']")))
        t = driver.find_element_by_xpath("//div[@id='sc_cit0']").text
        outcome0.append(t)
    except:
        exp.append(i)

with open('reference.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(outcome0))
with open('exp.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(exp))


