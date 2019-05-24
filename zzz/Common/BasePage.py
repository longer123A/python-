#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/16 21:33
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Common import logger
import logging
import time
import datetime
from Common.dir_config import screenshot_dir

class BasePage:
    def __init__(self,driverr):
        self.driver = driver

    #等待元素可见 - 失败的时候有截图有日志
    def wait_eleVisible(self,locator,wait_times=15,poll_frequency=0.5,model=""):
        """
        :param locator: 类型为元组(By.XXX,定位表达式)
        :return:
        """
        logging.info("等待元素可见。")
        try:
            #开始时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,wait_times,poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}: 元素 {1} 已可见,等待起始时间：{2},等待时长：{3}".format(model,locator,start,wait_times))
        except:
            #捕获异常到日志中；
            logging.exception("等待元素可见异常")
            #截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            #抛出异常
            raise

    # 等待元素存在
    def wait_elePrences(self, locator, wait=30, requence=0.5,model=""):
        # 等待元素存在- 等待的时间 起始时间/结束时间
        logging.info("等待元素存在。")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}: 元素 {1} 已存在,等待起始时间：{2},等待时长：{3}".format(model,locator, start, wait_times))
        except:
            # 日志
            logging.exception("等待元素存在异常")
            # 截图 - 图放哪儿去？图的名字？
            self._screenshot(model)
            raise

    #查找元素
    def get_element(self,locator,model=""):
        logging.info("{0}：开始查找元素：{1}".format(model,locator))
        try:
            return self.driver.find_element(*locator)
        except:
            pass
            # 捕获异常到日志中；
            logging.exception("查找元素失败：")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise
        # 查的多个元素

    def find_elements(self, locator,model=""):
        # 查找元素
        logging.info("{0}：开始查找符合表达式的所有元素：{1}".format(model,locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            logging.exception("查找元素失败。")
            self._screenshot(model)
            raise

    #输入操作
    def input_text(self,locator,text,model=""):
        #找到元素
        ele = self.get_element(locator, model)
        #输入操作
        logging.info("{0}: 元素：{1} 输入内容：{2}".format(model,locator,text))
        try:
            ele.send_keys(text)
        except:
            # 捕获异常到日志中；
            logging.exception("{0}: 元素：{1} 输入 {2} 操作失败：".format(model,locator,text))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

            #点击操作
    def click_element(self,locator,model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        #点击操作
        logging.info("{0}: 元素：{1} 点击事件。".format(model,locator))
        try:
            ele.click()
        except:
            # 捕获异常到日志中；
            logging.exception("元素：{0} 点击事件失败：".format(locator))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr_name,model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        # 获取元素的属性
        logging.info("{0}: 获取元素：{1} 的属性：{2}".format(model,locator,attr_name))
        try:
            value = ele.get_attribute(attr_name)
            logging.info("{0}: 元素：{1} 的属性：{2} 值为：{3}".format(model,locator,attr_name,value))
            return value
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的属性：{1} 失败，异常信息如下：".format(locator,attr_name))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise


    #获取元素的文本
    def get_text(self,locator,model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        # 获取元素的文本内容
        logging.info("{0}：获取元素：{1} 的文本内容".format(model,locator))
        try:
            text = ele.text
            logging.info("{0}：元素：{1} 的文本内容为：{2}".format(model,locator, text))
            return text
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的文本内容失败。报错信息如下：".format(locator))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    #滚动操作
    # 元素滚动操作
    def focus(self, locator, model=""):
        """
        """
        logging.info("{0}：滚动元素 {1} 到可见区域".format(model, locator))
        ele = self.get_element(locator, model)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        except:
            logging.exception("滚动失败")
            self._screenshot(model)
            raise



    def _screenshot(self,model_name):
        #时间
        # 文件格式 ：功能名称_年月日-时分秒.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        # 截图文件存放在 Screenshot目录下
        # driver方法：self.driver.save_screenshot()
        self.driver.save_screenshot(filePath)
        logging.info("截图成功，图片路径为：{0}".format(filePath))



    #上传操作
    # def upload(self):
    #     pass
    #
    # def focus(self):
    #     #找到元素
    #     #js语句执行
    #     pass
