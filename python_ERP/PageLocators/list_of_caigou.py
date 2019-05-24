#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xu
from selenium.webdriver.common.by import By

#采购单列表
class ListChas:

    sss=(By.XPATH,'//*[@name="query.supplierQuery.paymentMethod"]')
    sss2=(By.XPATH,'')
    #采购单列表
    list_chas = (By.XPATH,'//ul[@class="nav nav-tabs custom"]//*[@id="menu_11131000"]')

    #SKU
    list_sku = (By.XPATH,'//*[@id="product-sku"]')

    #搜索按钮
    seek_btn = (By.XPATH,'//*[@id="submitBtn"]')

    #第一个勾选按钮
    choose_btn = (By.XPATH,'//*[@id="data-list"]//tbody//tr[1]//td[1]//input[2]')

    #结款方式获取
    way_Money = '//table[@id="data-list"]//tbody//tr[1]//td[8]'

    #批量操作
    bulk_option = (By.XPATH,'//select[@class="form-control input-medium input-inline order-do"]')

    #批量是否可付款
    bulk_Money = (By.XPATH,'//select[@class="form-control input-medium input-inline order-do"]//optgroup//option[1]')

    #批量是否确认
    bulk_affirm = (By.XPATH, '//select[@class="form-control input-medium input-inline order-do"]//optgroup//option[2]')

    #修改采购订单
    modify_order = (By.XPATH,'//select[@class="form-control input-medium input-inline order-do"]//optgroup//option[6]')

    # 外部订单输入框
    input_order_number = (By.XPATH,'//input[@name="purchaseOrder.externalOrderId"]')

    #二次确认
    confir_ok = (By.XPATH,'//button[@data-id="ok"]')

    #快递
    express = (By.XPATH,'//table[@id="data-list"]//tbody//tr[1]//td[11]//a')
    input_express = (By.XPATH,'//textarea[@class="form-control"]')
    express_conf = (By.XPATH,'//button[@class="btn blue editable-submit"]')
    confirm_order = (By.XPATH,'//table[@id="data-list"]//tbody//tr[1]//td[13]//a[3]')

    # 外部订单号
    order_number = (By.XPATH,'//table[@id="data-list"]//tbody//tr[1]//td[9]')

    #订单号
    order_xuhao = (By.XPATH,'//*[@id="data-list"]/tbody/tr[1]/td[2]//div[1]')

    #订单编辑
    order_bji = (By.XPATH,'//*[@id="data-list"]//tbody//tr[1]//td[13]/a[4]')

    #编辑里面的外部订单号
    bji_order_number = (By.XPATH,'//*[@id="external-orderId"]')

    #编辑ok按钮
    bji_ok = (By.XPATH,'//*[@id="fixed-bottom"]//button')