#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xu
from selenium.webdriver.common.by import By

class KdiLeave:

    #订单管理
    order_guanli = (By.XPATH,'//*[@id="menu_12000000"]/a')

    #待合并
    dai_he = (By.XPATH,'//*[@id="menu_12111000"]/a')

    #快递等待打单
    dengdai_print = (By.XPATH,'//*[@id="menu_12181000"]/a')

    #按货打单
    anhuo_print = (By.XPATH,'//*[@id="menu_13151400"]/a')

    # 按框打单
    ankuang_print = (By.XPATH, '//*[@id="menu_13151500"]/a')

    #核对打单
    hedui_print = (By.XPATH, '//*[@id="menu_13151100"]/a')

    #多品打单
    duopin_print = (By.XPATH,'//*[@id="menu_13151300"]/a')

    #订单号筛选
    order_code_shai = (By.NAME,'query.searchType')
    order_code_shai2 = (By.XPATH, '//*[@id="search-type"]/option[2]')
    order_shai_value = (By.XPATH, '//*[@id="search-value"]')
    #搜索按钮
    seek_button = (By.XPATH,'//*[@id="searchForm"]//button[@type="submit"]')

    #快递——多品
    kdi_duop = (By.XPATH,'//*[@id="op-cell"]/button[1]')

    #快递——按货
    kdi_anh = (By.XPATH,'//*[@id="op-cell"]/button[2]')

    #快递——按框
    kdi_ank = (By.XPATH,'//*[@id="op-cell"]/button[3]')

    # 订单选择
    order_caoz = (By.XPATH, '//*[@name="orderIds"]')

    #当前选择
    choice = (By.XPATH,'//*[@id="submit-form"]//input[@value=3]')

    #OK
    ok_click = (By.XPATH,'//*[@data-id="ok"]')

    #订单移动
    order_move = (By.XPATH,'//*[@id="orderstatus-moving"]')

    #多仓库等待打单
    dengdai_print_duocang = (By.XPATH,'//*[@id="menu_12201100"]')

    #订单状态
    order_status= (By.XPATH,'//*[@id="order-list"]//tbody//tr[1]//td[3]//span')

    # 订单sku
    order_sku_qx = (By.XPATH, '//*[@id="order-list"]/tbody//tr[2]//td[5]//a')
    pass
