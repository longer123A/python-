#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/18 17:33

from selenium.webdriver.common.by import By
class BidPageLocator:
    # 投资输入框
    invest_input = (By.XPATH,'//input[@data-url="/Invest/invest"]')
    # 投资按钮
    invest_button = (By.XPATH,'//button[text()="投标"]')
    # 投资成功 - 查看并激活按钮
    active_button_in_successPopup = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败 - 弹出框 - 提示信息
    invest_failed_popup = (By.XPATH,'//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]')
    # 投资失败 - 弹出框 - 关闭弹出框
    invest_close_failed_popup_button = (By.XPATH,'//div[contains(@class,"layui-layer-dialog")]//a')