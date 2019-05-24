#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/18 17:31
from selenium.webdriver.common.by import By
class IndexPageLocator:
    #用户昵称
    user_nick = (By.XPATH,'//a[@href="/Member/index.html"]')
    #标名称
    bid_name_loc =(By.XPATH,'//a[text()="抢投标"]')