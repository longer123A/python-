#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xu
from selenium.webdriver.common.by import By


class NoGoode:
    # 收发货管理
    receive_dispatch = (By.XPATH, '//*[@id="menu_13000000"]')
    #QC不良品
    qc_nocoode = (By.XPATH,'//*[@id="menu_13120000"]//*[@id="menu_13121500"]')

    #sku
    sku = (By.XPATH,'//*[@id="product-sku"]')

    #搜索按钮
    seek_button = (By.XPATH,'//*[@id="search-form"]//button[1]')

    #日志按钮
    logs_button = (By.XPATH,'//form[@name="submitForm"]//tbody//tr[1]//td[13]//a[4]')

    #内容
    get_text = (By.XPATH,'//*[@id="data-list"]/tbody/tr[1]/td[12]')

    #序号输入
    input_xuhao = (By.XPATH,'//*[@name="query.purchaseOrder.purchaseOrder"]')


    #等待QC
    wait_qc = (By.XPATH,'//*[@id="menu_13120000"]//*[@id="menu_13121100"]')

    #已废弃
    feiqi_order = (By.XPATH,'//*[@id="instock-nav"]/li[10]/a')

    #待采购
    dai_caigou = (By.XPATH,'//*[@id="instock-nav"]/li[5]/a')
    dai_caigou_text =(By.XPATH,'//*[@id="data-list"]/tbody/tr[1]/td[14]')