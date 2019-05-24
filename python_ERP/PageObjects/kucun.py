#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from python_ERP.Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import logging
from python_ERP.Common import logger
class KuCun(BasePage):

    #获取开始库存和最后库存，进行断言
    def get_kucun(self,sku):
        logging.info('获取开始库存或最后库存')
        self.click_element((By.XPATH,'//*[@id="menu_11000000"]'),model='点击库存管理')

        # 点击大浪仓库
        self.click_element((By.XPATH, '//*[@id="menu_11110000_false_01"]/a'),model='点击大浪仓库')

        #输入SKU

        self.input_text((By.XPATH, '//*[@id="product-sku"]'),sku,model='输入SKU')

        #点击搜索
        self.click_element((By.XPATH, '//*[@id="search-form"]/div/div[2]/button[1]'),model='点击搜索')

        time.sleep(3)
        #
        return int(self.get_text((By.XPATH, '//table[@id="data-list"]/tbody//tr[1]//td[8]'),model='返回库存'))