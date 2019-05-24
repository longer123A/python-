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
    order_choose = (By.XPATH,'//input[@name="orderIds"]')

    #平台订单号
    pingtai_code = (By.XPATH,'//*[@id="search-type"]')

    #订单选择
    order_caoz = (By.XPATH,'//*[@id="order-list"]//tbody//tr[1]//label')

    #运费估算
    freight_gu = (By.XPATH,'//*[@title="运费估算"]')

    #修改订单
    order_xiug = (By.XPATH,'//*[@title="修改订单"]')

    #跟踪号
    order_geng = (By.XPATH,'//*[@id="order-tranking"]')

    #快递筛选(快递)
    express_shai = (By.XPATH,'//select[@name="transportationModeQueryCondition.logisticsType"]')
    seek_button = (By.XPATH,'//*[@id="submit-form"]//div[9]')


    xinxi = (By.XPATH,'//*[@id="data-list"]/tbody/tr[1]/td[1]')

    #确定按钮
    ok_button = (By.XPATH,'//*[@data-id="ok"]')

    #搜索订单
    sousuo_order = (By.XPATH,'//*[@name="query.criteria"]')

    #搜索按钮
    sousuo_button = (By.XPATH,'//*[@class="btn btn-default"]')

    #订单移动
    dingdan_move = (By.XPATH,'//*[@id="orderstatus-moving"]')
    #待合并
    wait_he = (By.XPATH,'//*[@id="orderstatus-moving"]/optgroup[1]/option[1]')
    #等待打单
    wati_dengdai = (By.XPATH,'//*[@id="orderstatus-moving"]/optgroup[5]/option[1]')
    #按货打单
    anhuo_print = (By.XPATH,'//*[@id="orderstatus-moving"]/optgroup[5]/option[2]')
    #按框打单
    ankuang_print = (By.XPATH, '//*[@id="orderstatus-moving"]/optgroup[5]/option[3]')
    #核对打单
    hedui_print = (By.XPATH, '//*[@id="orderstatus-moving"]/optgroup[5]/option[4]')
    # 核对打单
    duopin_print = (By.XPATH, '//*[@id="orderstatus-moving"]/optgroup[5]/option[5]')

    #运输方式
    yunshu_mode = (By.XPATH,'//*[@name="transportationModeQueryCondition.logisticsType"]')

    #快递搜索
    kdi_sousuo = (By.XPATH,'//*[@id="submit-form"]/div[9]/button')

    #查询订单号
    chaxun_code = (By.XPATH,'//*[@placeholder="系统订单号|平台订单号"]')
    code_button = (By.XPATH,'//*[@class="btn btn-default"]')

    #运输方式
    kdi_moth = (By.XPATH,'//*[@id="select2-chosen-5"]')
    input_moth = (By.XPATH,'//*[@id="s2id_autogen5_search"]')
    click_moth = (By.XPATH,'//*[@id="select2-results-5"]//ul')

    #确认修改跟踪号
    gen_code_od = (By.XPATH,'//*[@id="fixed-bottom"]//button')

    #订单状态
    order_statu = (By.XPATH,'//*[@id="order-list"]//tbody//tr[1]//td[3]//span')

    #订单运费
    order_money = (By.XPATH,'//*[@id="order-list"]//td[8]')

    #订单操作
    order_caozou = (By.XPATH,'//*[@id="top_tool_bar"]/tbody//select[4]')

    #新运费
    xin_yunfei = (By.XPATH,'//*[@name="orders[0].freight"]')

    #权限运输方式
    yunshu_moth = (By.XPATH, '//*[@id="select2-chosen-4"]')
    input_moth_qx = (By.XPATH, '//*[@id="s2id_autogen4_search"]')
    click_moth_qx = (By.XPATH, '//*[@id="select2-results-4"]//ul')
