#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 16:17

from PageLocators.bid_page_locator import BidPageLocator as loc
from Common.BasePage import BasePage
class BidPage(BasePage):

    #获取用户余额
    def get_user_leftMoney(self):
        name = "标页面_获取用户余额"
        #等待
        self.wait_eleVisible(loc.invest_input,model=name)
        # 获取金额输入框的data-amount属性值;
        return self.get_element_attribute(loc.invest_input,"data-amount",model=name)

    #投资操作
    def invest(self,money):
        name = "标页面_投资操作"
        #输入框，输入值
        self.wait_eleVisible(loc.invest_input,model=name)
        self.input_text(loc.invest_input,money,model=name)
        # 点击按钮
        self.click_element(loc.invest_button,model=name)

    #投资成功 - 弹出框 - 点击激活并查看按钮
    def click_activeButton_from_investSuccess_popup(self):
        name = "标页面_投资成功弹出框_点击查看并激动按钮"
        self.wait_eleVisible(loc.active_button_in_successPopup,model=name)
        self.click_element(loc.active_button_in_successPopup,model=name)

    #投资失败 - 2种场景

    # 投资失败的弹出框 - 获取信息
    def get_errorMsg_from_popup(self):
        name = "投资失败弹出框_提示信息"
        self.wait_eleVisible(loc.invest_failed_popup, model=name)
        msg = self.get_text(loc.invest_failed_popup, model=name)
        # 关闭弹出框
        self.click_element(loc.invest_close_failed_popup_button, model=name)
        return msg