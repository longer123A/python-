#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from selenium.webdriver.common.by import By
class SetPageLocator:
    # 选择平台
    choose_platform = (By.XPATH,'//*[@id="platform-id"]')
    #订单号
    order_input = (By.XPATH,'//*[@id="platform-order-id"]')
    #选择货币
    choose_currency = (By.XPATH,"//select[@class='input-xsmall  input-inline form-control']")
    #选择物流
    choose_logistics = (By.XPATH,"//select[@name='order.logisticsType']")
    #选择日期
    choose_data = (By.XPATH,"//input[@name='order.paidDate']")
    #日期确认
    data_affirm = (By.XPATH,'//*[@id="dpOkInput"]')


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~
    #添加商品
    add_goods= (By.XPATH,'//*[@id="editable-new"]')
    #SKU1
    SKU_1 = (By.XPATH,'//*[@id="item-sku-0"]')
    #数量1
    quantity = (By.XPATH,"//input[@name='order.orderItems[0].saleQuantity']")
    #单价1
    unit_price = (By.XPATH,"//input[@name='order.orderItems[0].productPrice']")

    # SKU2
    SKU_2 = (By.XPATH,'//*[@id="item-sku-1"]')
    # 数量1
    quantity2 = (By.XPATH,"//input[@name='order.orderItems[1].saleQuantity']")
    # 单价1
    unit_price2 = (By.XPATH,"//input[@name='order.orderItems[1].productPrice']")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #收件人
    recipients = (By.XPATH,'//input[@name="order.buyerName"]')
    #买家ID
    buyer_ID = (By.XPATH,'//input[@name="order.buyerId"]')
    #Email
    Email_input = (By.XPATH,'//input[@name="order.buyerEmail"]')
    #国家
    choose_state = (By.XPATH,'//select[@name="order.buyerCountryCode"]')
    #州
    choose_province = (By.XPATH,'//input[@name="order.buyerStateOrProvince"]')
    #City
    choose_city = (By.XPATH,'//input[@name="order.buyerCity"]')
    #街道
    choose_street = (By.XPATH,'//input[@name="order.street"]')
    #邮编
    choose_code = (By.XPATH,'//input[@name="order.buyerPostalCode"]')
    #电话
    tel = (By.XPATH,'//input[@name="order.buyerTel"]')
    # ~~~~~~~~~~~~~~~~~~~~~
    put_button = (By.XPATH,'//*[@id="fixed-bottom"]//button')