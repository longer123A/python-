#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

from python_ERP1.Common.BasePage import BasePage
from python_ERP1.PageLocators.set_page_order import SetPageLocator as loc
from python_ERP1.TestDatas import set_data as data

class SetPage(BasePage):


    get_data = data.information
    # ['AliExpress', 528060, '许寿龙', 'China(中国CN)', '广东省', '民治街道天上人间休闲会所', '518000']
    # 填写订单信息
    def fill_order_information(self):
        name = "填写订单信息"

        # 等待元素
        self.wait_eleVisible(loc.put_button, model=name)
        #选择平台
        self.select(loc.choose_platform,self.get_data[0],model='选择平台')
        #输入订单号
        self.input_text(loc.order_input,self.get_data[1],model='输入订单号')
        #选择货币
        self.select(loc.choose_currency,'AED',model='选择货币')
        #选择物流
        self.select(loc.choose_logistics,'4PX物流-新加坡挂号',model='选择物流')
        #付款时间
        self.switchover_html(loc.choose_data,loc.data_affirm,0,model='付款时间选择')



