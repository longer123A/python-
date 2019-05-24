#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

from selenium.webdriver.common.by import By
#订单管理locator
class OrderMana:
    # 新建订单按钮
    order_button = (By.XPATH,"//div[@class='pull-left']")

    #订单管理
    mana_nick = (By.XPATH,'//*[@id="menu_12000000"]')

    #订单号元素
    order_code = (By.XPATH,'//input[@name="orderIds"]')