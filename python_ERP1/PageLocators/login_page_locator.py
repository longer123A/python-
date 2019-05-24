#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

#登录locator
from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 元素定位
    # 用户名输入框
    user_input = (By.XPATH,'//*[@id="username"]')
    # 密码输入框
    passwd_input = (By.XPATH,'//*[@id="password"]')
    #验证码输入框
    code_input= (By.XPATH,'//*[@id="captcha"]')
    # 登陆按钮
    login_button = (By.XPATH,'//*[@id="login-btn"]')


