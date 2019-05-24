#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
#建议采购页面
from selenium.webdriver.common.by import By
class SuPusing:

    shouji = (By.XPATH,'//*[@name="query.product.productName"]')
    #结款方式
    money_yue = '月结'
    money_yue1 = '半月结'
    money_zhou = '周结'
    #上下架
    status = (By.XPATH,'//*[@name="query.listingStatus"]')
    #是否在途
    way_tu = (By.XPATH,'//*[@name="query.hasInTransit"]')
    #结款方式
    money_way = (By.XPATH,'//*[@name="query.supplierQuery.paymentMethod"]')

    #SKU
    SKU = (By.XPATH,'//*[@id="data-list"]//tr[1]//label//a')

    #采购数量
    order_size = (By.XPATH,'//*[@id="data-list"]//tr[1]//td[18]//input[2]')

    #选择按钮
    sp_choose = (By.XPATH,'//input[@name="checkedSkuList"]')

    #生成采购单
    # chase_order = (By.XPATH,'//*[@id="purchase-form"]//button[1]')

    #sku输入
    input_sku = (By.XPATH,'//*[@id="product-sku"]')

    #点击搜索按钮//i[@class="icon-search"]
    seek_button = (By.XPATH,'//i[@class="icon-search"]')

    #生成采购订单//*[@id="purchase-form"]//button[1]
    gen_chase_order = (By.XPATH,'//*[@id="purchase-form"]//button[1]')
