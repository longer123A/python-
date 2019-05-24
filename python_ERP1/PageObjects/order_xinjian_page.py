#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

from python_ERP1.PageLocators.order_mana_xinjian import OrderMana as loc
from python_ERP1.Common.BasePage import BasePage
class OrderPage(BasePage):

    #获取订单号
    def get_order_number(self):
        name = "获取订单号"
        #等待元素可见
        self.wait_eleVisible(loc.order_code,model=name)
        # 获取订单的value值;
        return self.get_element_attribute(loc.order_code,"value",model=name)


    #点击新建订单按钮
    def new_order(self):
        name = "点击新建订单按钮"
        self.wait_eleVisible(loc.order_button,model=name)
        self.click_element(loc.order_button,model=name)

    #窗口切换
    def window_switch_order(self,index):
        name = '窗口切换'
        self.window_switch(index,model=name)

    #