#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from selenium.webdriver.common.action_chains import ActionChains
from python_ERP.PageLocators.login_page_locator import LoginPageLocator as loc
from python_ERP.Common.BasePage import BasePage
import time
import logging
from python_ERP.Common import logger

class LoginPage(BasePage):

    # 登陆功能
    def login(self,username):
        #日志内容：登陆页面的登陆功能
        logging.info("登陆页面_登陆功能")
        self.input_text(loc.user_input,username,model='输入用户名')
        self.input_text(loc.passwd_input,111,model='输入密码')
        self.input_text(loc.code_input,1111,model='输入验证码')
        self.click_element(loc.login_button,model='点击登录按钮')
        time.sleep(2)

    def clear_login(self):
        time.sleep(1)
        logging.info("切换账号")
        ele=self.get_element(loc.use,model='点击用户')
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(1)
        try:
            self.click_element(loc.quit_use,model='点击用户')
            time.sleep(3)
        except:
            self.click_element(loc.use,model='点击注销用户')
            time.sleep(1)
            self.click_element(loc.quit_use, model='退出')
            time.sleep(3)