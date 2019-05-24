#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import datetime
from python_ERP.Common.dir_config import screenshot_dir
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
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
            #截图 - 保存到的指定的目录。
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
            # 捕获异常到日志中；
            logging.exception("查找元素失败：")
            # 截图 - 保存到的指定的目录。
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
        self.wait_eleVisible(locator, model=model)
        ele = self.get_element(locator, model)
        #输入操作
        logging.info("{0}: 元素：{1} 输入内容：{2}".format(model,locator,text))
        try:
            ele.clear()
            ele.send_keys(text)
        except:
            # 捕获异常到日志中；
            logging.exception("{0}: 元素：{1} 输入 {2} 操作失败：".format(model,locator,text))
            # 截图 - 保存到的指定的目录
            self._screenshot(model)
            # 抛出异常
            raise

            #点击操作
    def click_element(self,locator,model=""):
        self.wait_eleVisible(locator, model=model)
        # 找到元素
        ele = self.get_element(locator, model)
        #点击操作
        logging.info("{0}: 元素：{1} 点击事件。".format(model,locator))
        try:
            ele.click()
        except:
            # 捕获异常到日志中；
            logging.exception("元素：{0} 点击事件失败：".format(locator))
            # 截图 - 保存到的指定的目录。
            self._screenshot(model)
            # 抛出异常
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr_name,model=""):
        # 找到元素
        self.wait_eleVisible(locator, model=model)
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
            # 截图 - 保存到的指定的目录。
            self._screenshot(model)
            # 抛出异常
            raise

    #select列表操作
    def select(self,locator,get_text,model=""):
        """
        :param locator: select列表元素
        :param get_text: 选择的内容
        """
        logging.info("{0}:{1}select列表操作".format(locator,model))
        self.wait_eleVisible(locator, model=model)
        ele = self.get_element(locator,model)
        try:
            s = Select(ele)
            time.sleep(1)
            s.select_by_visible_text(get_text)
            time.sleep(0.5)
            logging.info('select列表操作完毕{0}'.format(get_text))
        except:
            logging.exception('select列表操作失败')
            self._screenshot(model)
            raise

    #切换HTML页面
    def switchover_html(self,indexes,model=''):
         # :param table: 触发另一个HTML页面条件
         # :param locator: 需要操作的元素
         # :indexes: 索引值
        logging.info("{0}切换HTML页面".format(model))
        try:
            self.driver.switch_to.frame(indexes)
            logging.info('HTML页面切换成功')
            # self.driver.switch_to.default_content()
            # logging.info('HTML页面切回成功')
        except:
            logging.exception('HTML切换失败')
            self._screenshot(model)
            raise

    #窗口切换
    def window_switch(self,index,model=''):
        logging.info("切换窗口位置{0}，功能点{1}".format(index,model))
        try:
            cur_handles = self.driver.window_handles
            self.driver.switch_to.window(cur_handles[index])
            logging.info("窗口切换成功")
        except:
            logging.exception('窗口切换失败')
            self._screenshot(model)
            raise

    # 获取元素的文本
    def get_text(self, locator, model=""):
        # 找到元素
        self.wait_eleVisible(locator, model=model)
        ele = self.get_element(locator, model)
        # 获取元素的文本内容
        logging.info("{0}：获取元素：{1} 的文本内容".format(model, locator))
        try:
            text = ele.text
            logging.info("{0}：元素：{1} 的文本内容为：{2}".format(model, locator, text))
            return text
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的文本内容失败。报错信息如下：".format(locator))
            # 截图 - 保存到的指定的目录
            self._screenshot(model)
            # 抛出异常
            raise
    #截图
    def _screenshot(self,model_name):
        #时间
        # 文件格式 ：功能名称_年月日-时分秒.png
        filePath = screenshot_dir + "/xu_{0}_{1}.png".format(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()),model_name)
        # 截图文件存放在 Screenshot目录下
        # driver方法：self.driver.save_screenshot()
        self.driver.save_screenshot(filePath)
        logging.info("截图成功，图片路径为：{0}".format(filePath))


    # 元素滚动操作
    def roll(self, locator, model="页面滚动"):
        logging.info('开始滚动页面：{0}'.format(locator))
        try:
            js = 'var q=document.documentElement.scrollTop=%s' %locator
            self.driver.execute_script(js)
            logging.info('页面滚动成功：{0}'.format(locator))
        except:
            logging.exception('页面滚动失败')
            self._screenshot(model)
            raise


        #     """
        #     """
        #     logging.info("{0}：滚动元素 {1} 到可见区域".format(model, locator))
        #     ele = self.get_element(locator, model)
        #     try:
        #         self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        #     except:
        #         logging.exception("滚动失败")
        #         self._screenshot(model)
        #         raise

    #alert弹窗处理
    def get_alert(self,model=''):
        logging.info('{0}弹窗处理'.format(model))
        try:
            WebDriverWait(self.driver,5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            logging.info('alert弹窗处理完成')
        except:
            logging.exception('alert弹窗处理失败')
            self._screenshot(model)
            raise

    #判断元素是否存在
    def isElementExist(self, element,model='元素不存在'):

        logging.info('判断元素是否存在{0}'.format(element))
        try:
            self.driver.find_element_by_xpath(element)
            # self.driver.find_element_by_xpath(element)
            logging.info('元素存在')
            return True

        except:
            logging.info(model)
            return False

    #判断元素是否可见
    def isElementExist_2(self, element):
        logging.info('判断元素是否可见{0}'.format(element))
        try:

            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,element)))
            logging.info('元素不可见')
            return True

        except:
            logging.info('元素不可见')
            return False

    #获取结款方式
    def get_money_way(self,element):
        logging.info('判断结款方式是否可见{0}'.format(element))
        text_1 = str(self.driver.find_element_by_xpath(element).text)
        try:
            if  text_1 in ["阿里账期",'线上现结']:
                logging.info('类型{0}'.format(type(text_1)))
                logging.info('结款方式阿里线上：{0}'.format(text_1))
                return True
            else:
                logging.info('结款方式：{0}'.format(text_1))
                return False
        except:
            logging.info('结款方式获取失败')
            self._screenshot('结款方式获取失败')

