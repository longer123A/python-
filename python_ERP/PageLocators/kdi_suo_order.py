#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xu
from selenium.webdriver.common.by import By

class SuoOrder:

    #收发货管理
    start_guanli = (By.XPATH,'//*[@id="menu_13000000"]')

    #按货打单
    anhuo_print = (By.XPATH, '//*[@id="menu_13101500"]/a')
    kdi_anhuo_print = (By.XPATH,'//*[@id="menu_13151400"]/a')
    zyun_anhuo_print = (By.XPATH,'//*[@id="menu_13171300"]/a')
    #按框打单
    ankuang_print = (By.XPATH, '//*[@id="menu_13101800"]/a')
    kdi_ankuang_print = (By.XPATH,'//*[@id="menu_13151500"]/a')

    #核对打单
    kdi_hedui_print = (By.XPATH,'//*[@id="menu_13151100"]/a')

    #多品打单
    duopin_print = (By.XPATH, '//*[@id="menu_13101900"]/a')
    kdi_duopin_print = (By.XPATH,'//*[@id="menu_13151300"]/a')
    zyun_duopin_print = (By.XPATH,'//*[@id="menu_13171400"]/a')
    #多仓库打单
    duocang_print = (By.XPATH,'//*[@id="menu_13191000"]/a')

    #订单号筛选
    order_code_shai = (By.NAME,'query.searchType')
    order_shai_value = (By.XPATH, '//*[@name="query.searchValue"]')
    #搜索按钮
    seek_button = (By.XPATH,'//*[@id="searchForm"]//button[@type="submit"]')

    # 订单选择
    order_caoz = (By.XPATH, '//*[@name="orderIds"]')

    # 当前选择
    choice = (By.XPATH, '//*[@id="submit-form"]//input[@value=3]')

    #锁单
    anhuo_suo_order = (By.XPATH,'//div[@class="pull-left"]//button[1]')

    # OK
    ok_click = (By.XPATH, '//*[@data-id="ok"]')