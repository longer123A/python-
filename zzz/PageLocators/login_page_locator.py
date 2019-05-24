#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 22:17
from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 元素定位
    # 用户名输入框
    user_input = (By.XPATH,"//input[@name='phone']")
    #user_input_v2 =(By.XPATH,"//input[@name='phone']")
    # 密码输入框
    passwd_input = (By.XPATH,"//input[@name='password']")
    # 登陆按钮
    login_button = (By.XPATH,"//button[@type='button']")
    # 没有用户名、没有密码、错误的用户名格式错误提示框
    error_prompt_fromLoginArea = (By.XPATH,'//div[@class="form-error-info"]')
    # 用户名或者密码错误的提示框
    wrongData_msg_xpath = (By.XPATH,'//div[@class="layui-layer-content"]')


