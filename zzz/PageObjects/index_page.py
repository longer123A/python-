#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 21:00

from Common.BasePage import BasePage
from PageLocators.index_page_locator import IndexPageLocator as loc
class IndexPage(BasePage):
    bid_name_loc = '//*[@class="fs-22"]'

    # 获取用户昵称值
    def get_nickName(self):
        name = "首页_获取用户昵称"
        # 等待
        self.wait_eleVisible(loc.user_nick, model=name)
        return self.get_text(loc.user_nick, model=name)

    # 点击第一个标的抢投标按钮
    def click_first_investButton(self):
        name = "首页_点击第一个抢投标"
        self.wait_eleVisible(loc.bid_name_loc, model=name)
        self.click_element(loc.bid_name_loc, model=name)

