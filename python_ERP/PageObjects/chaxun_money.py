#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
import time
import re
from selenium.webdriver.common.by import By
from python_ERP.Common.BasePage import BasePage
import logging
from python_ERP.Common.logger import *

class SkuChaxun(BasePage):

    #仓库管理//*[@id="menu_11000000"]
    #sku列表
    #sku
    #搜索按钮
    def money(self,sku):
            """

            :param sku: 根据sku查询商品的价格
            :return:     返回商品的价格
            """

            cur_handles = self.driver.window_handles
            self.driver.switch_to.window(cur_handles[0])
            nama = '查询价格'
            #需要转至第一窗口
            #库存管理
            kucun = (By.XPATH,'//*[@id="menu_11000000"]')
            self.click_element(kucun,model=nama)
            #sku列表
            sku_list = (By.XPATH,'//*[@id="menu_11101200"]')
            self.click_element(sku_list,model=nama)
            time.sleep(2)

            self.driver.switch_to.frame(0)
            #sku列表
            sku_loc=(By.XPATH,'//*[@id="product-sku"]')
            self.input_text(sku_loc,sku,model=nama)
            #搜索按钮
            seek_button = (By.XPATH,'//*[@class="icon-search"]')
            self.click_element(seek_button,model=nama)
            # driver.find_element_by_xpath('').click()
            time.sleep(2)
            self.driver.switch_to.default_content()
            js = "var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(js)
            self.driver.switch_to.frame(0)

            #点击更多按钮
            get_all = (By.XPATH,'//*[@id="data-list"]//span[51]/a')
            self.click_element(get_all,model=nama)
            # driver.find_element_by_xpath(').click()
            self.driver.switch_to.default_content()
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(js)
            self.driver.switch_to.frame(0)

            #获取全部文本内容
            get_text = (By.XPATH,'//*[@id="data-list"]//td[4]/div[2]')
            s=self.get_text(get_text,model=nama)
            # s=driver.find_element_by_xpath('').text
            time.sleep(3)
            name_score_list=s.split('\n')
            logging.info('ssss:{0}'.format(name_score_list))

            name_score_list_string = ",".join(name_score_list)
            s = re.findall(r"\d+", name_score_list_string)
            score_list_int = list(map(int, s))
            self.driver.switch_to.default_content()
            self.driver.switch_to.window(cur_handles[-1])
            return max(score_list_int)



if __name__ == '__main__':
    print(money())