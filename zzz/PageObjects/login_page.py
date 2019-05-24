#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 20:59

from PageLocators.login_page_locator import LoginPageLocator as loc
from Common.BasePage import BasePage

class LoginPage(BasePage):

    # 登陆功能
    def login(self,username,passwd):
        #日志内容：登陆页面的登陆功能
        name = "登陆页面_登陆功能"
        self.wait_eleVisible(loc.user_input,model=name)
        self.input_text(loc.user_input,username,model=name)
        self.input_text(loc.passwd_input,passwd,model=name)
        self.click_element(loc.login_button,model=name)

    def get_errorMsg_fromLoginArea(self):
        name="登陆页面_登陆区域错误提示"
        return self.get_text(loc.error_prompt_fromLoginArea,model=name)

    def get_errorMsg_from_pageCenter(self):
        name = "登陆页面_获取页面正中间错误信息"
        self.wait_eleVisible(loc.wrongData_msg_xpath, model=name, poll_frequency=0.2)
        return self.get_text(loc.wrongData_msg_xpath, model=name)

    def register(self):
        pass