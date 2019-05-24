#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 16:23

from Common.BasePage import BasePage
from PageLocators.user_page_locator import UserPageLocator as loc

class UserPage(BasePage):

    # 获取用户余额
    def get_user_leftMoney(self):
        name = "个人页面_获取用户余额"
        # 等待元素
        self.wait_eleVisible(loc.user_money, model=name)
        # 获取个人可用余额的文本内容
        text = self.get_text(loc.user_money, model=name)
        # 截取数字部分 - 分隔符为 元
        return text.strip("元")

    # 获取第一条投资记录的时间、投资金额、收益金额 -- 扩展
    # def get_first_investRecord_info(self):
    #     pass