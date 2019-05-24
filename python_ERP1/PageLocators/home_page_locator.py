#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from selenium.webdriver.common.by import By

#首页locator
class HomePageLocator:
    #待合并按钮
    merge_nick= (By.XPATH,'//*[@id="status-deliver"]/a[2]')
    #首页按钮
    home_nick =(By.XPATH,"//a[text()='首页']")