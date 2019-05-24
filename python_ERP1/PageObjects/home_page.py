#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

from python_ERP1.Common.BasePage import BasePage
from python_ERP1.PageLocators.home_page_locator import HomePageLocator as loc
class HomePage(BasePage):

    #点击待合并按钮
    def click_to_merge(self):
        nama="点击待合并按钮"
        self.wait_eleVisible(loc.merge_nick, model=nama)
        self.click_element(loc.merge_nick,model=nama)


    # 点击首页按钮
    def click_first_investButton(self):
        name = "点击首页按钮"
        self.wait_eleVisible(loc.home_nick, model=name)
        self.click_element(loc.home_nick, model=name)

