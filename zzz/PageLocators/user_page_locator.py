#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/18 17:36
from selenium.webdriver.common.by import By
class UserPageLocator:
    # 个人可用余额
    user_money = (By.XPATH,'//*[@class="personal_info"]//li[@class="color_sub"]')