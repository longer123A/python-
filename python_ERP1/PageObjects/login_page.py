#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

from python_ERP1.PageLocators.login_page_locator import LoginPageLocator as loc
from python_ERP1.Common.BasePage import BasePage

class LoginPage(BasePage):

    # 登陆功能
    def login(self,username,passwd,code):
        #日志内容：登陆页面的登陆功能
        name = "登陆页面_登陆功能"
        self.wait_eleVisible(loc.user_input,model=name)
        self.input_text(loc.user_input,username,model=name)
        self.input_text(loc.passwd_input,passwd,model=name)
        self.input_text(loc.code_input,code,model=name)
        self.click_element(loc.login_button,model=name)


if __name__ == '__main__':
    LoginPage().login('it_test','1','1')
