#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xu
from selenium.webdriver.common.by import By
from python_ERP.PageLocators.kdi_locator import KdiLeave as loc
from python_ERP.PageLocators.kdi_suo_order import SuoOrder as loa
from python_ERP.Common.BasePage import BasePage
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import logging
from python_ERP.Common import logger


class KdiLeavePage(BasePage):

    #"待合并——等待打单"
    def he_move_dengdai(self,code):
        """
        :param code:  平台订单号，查询唯一订单
        """
        logging.info('模块："待合并——等待打单"')
        #订单条件筛选
        self.click_element(loc.order_guanli,model='订单管理按钮')                         #order_guanli：订单管理按钮
        self.click_element(loc.dai_he,model='订单管理待合并按钮')                               #dai_he：订单管理下的待合并按钮
        time.sleep(2)
        self.select(loc.order_code_shai,'平台订单号',model='选择select列表的平台订单号')                #order_code_shai：选择查询的单号类型
        time.sleep(1)
        self.input_text(loc.order_shai_value,code,model='输入平台订单号')                   #输入平台订单号
        time.sleep(1)
        self.click_element(loc.seek_button,model='点击订单按钮')                          #seek_button：搜索按钮


        time.sleep(2)
        self.click_element(loc.order_caoz,model='勾选第一个订单')                           #order_caoz：勾选订单
        time.sleep(0.5)
        self.click_element(loc.kdi_duop,model='点击一键移动至等待打单')                             #从待合并状态----等待打单（命名是由于元素相等）


        self.switchover_html(1)
        time.sleep(0.5)
        self.click_element(loc.choice,model='当前选择')                               #当前选择操作
        self.driver.switch_to.default_content()
        self.click_element(loc.ok_click,model='确认当前选择')                             #确认操作
        time.sleep(2)


    #快递等待打单-打单
    def dengdai_move_print(self,code,moth):
        logging.info('模块：快递等待打单-打单,打单方式为{0}'.format(moth))
        self.click_element(loc.order_guanli,model='点击订单管理按钮')                         #订单管理按钮
        self.click_element(loc.dengdai_print,model='点击等待打单按钮')                        #等待打单
        time.sleep(2)
        self.select(loc.order_code_shai, '平台订单号', model='选择select列表的平台订单号')              #筛选平台订单号
        time.sleep(1)
        self.input_text(loc.order_shai_value, code, model='输入平台订单号')                 #输入平台订单号
        time.sleep(1)
        self.click_element(loc.seek_button,model='点击搜索按钮')                          #点击搜索按钮
        time.sleep(2)
        self.click_element(loc.order_caoz,model='勾选第一个按钮')                           #勾选第一个订单
        if moth=='多品打单':
            self.click_element(loc.kdi_duop,model='一键移动至多品打单')                         #移动至多品打单
            time.sleep(1)
            self.switchover_html(1)
            self.click_element(loc.choice, model='点击当前选择')                          #选择当前选择
            self.driver.switch_to.default_content()
            self.click_element(loc.ok_click, model='当前选择确认')                        #点击确认
            time.sleep(2)
        elif moth=='按货打单':
            self.click_element(loc.kdi_anh, model='一键移动至按货打单')                          #移动至按货打单
            time.sleep(1)
            self.switchover_html(1)
            self.click_element(loc.choice, model='点击当前选择')                          #选择当前选择
            self.driver.switch_to.default_content()
            self.click_element(loc.ok_click, model='当前选择确认')                         #点击确认
            time.sleep(2)

        elif moth=='按框打单':
            self.click_element(loc.kdi_ank, model='一键移动至按框打单')                        #移动至按框打单
            time.sleep(1)
            self.switchover_html(1)
            self.click_element(loc.choice, model='点击当前选择')                         #选择当前选择
            self.driver.switch_to.default_content()
            self.click_element(loc.ok_click, model='当前选择确认')                        #点击确认
            time.sleep(2)
        else:
            self.select(loc.order_move,'快递-核对打单',model='移动至核对打单')            #移动至-核对打单
            self.get_alert(model='确认移动至核对打单')                                        #弹窗处理
            time.sleep(1)
            self.click_element(loc.ok_click,model='确认提示语')                       #确认
            time.sleep(2)

    #打单——锁单
    def dadna_move_suo(self,code,moth):
        nama = '{0}到锁单'.format(moth)
        self.click_element(loa.start_guanli,model='点击收发货管理')                        #点击收发货管理
        if moth=="按货打单":
            self.click_element(loa.kdi_anhuo_print,model='点击快递—按货打单按钮')                     #点击快递—按货打单按钮
            time.sleep(2)
            self.select(loa.order_code_shai,'平台订单号',model='筛选条件为平台订单号')           #筛选条件为平台订单号
            self.input_text(loa.order_shai_value,code,model='输入平台订单号')              #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button,model='点击搜索按钮')                     #点击查询按钮
            time.sleep(2)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            self.click_element(loa.order_caoz,model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order,model='点击锁定订单按钮')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice,model='当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click,model='当前选择确认按钮')                        #确认按钮

            return self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')   #返回SKU，用于扫描
        elif moth=="按框打单":
            self.click_element(loa.kdi_ankuang_print, model='点击快递—按框打单')                   #点击快递—按框打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')          #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击搜索按钮')                     #点击查询按钮
            time.sleep(2)
            self.click_element(loa.order_caoz, model='勾选当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='当前选择确认按钮')                        #确认按钮
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            return self.get_text((By.XPATH,'//*[@id="order-list"]//tr[2]//td[5]'),model='返回SKU')      #返回SKU，用于扫描
        elif moth=="多品打单":
            self.click_element(loa.kdi_duopin_print, model='点击快递—多品打单')                     #点击快递—多品打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')            #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击搜索按钮')                     #点击查询按钮

            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)

            time.sleep(2)
            self.click_element(loa.order_caoz, model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='当前选择确认按钮')                         #确认按钮
            return self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')        #返回SKU，用于扫描
        else:
            print('输出错误')


    #多仓等待打单---多仓打单
    def dengdai_move_duoca(self,code):
        logging.info('模块：多仓等待打单---多仓打单')
        self.click_element(loc.order_guanli, model='订单管理按钮')  # 订单管理按钮
        time.sleep(1)
        self.click_element(loc.dengdai_print_duocang, model='等待打单')  # 等待打单
        time.sleep(2)
        self.select(loc.order_code_shai, '平台订单号', model='筛选平台订单号')  # 筛选平台订单号
        time.sleep(1)
        self.input_text(loc.order_shai_value, code, model='输入平台订单号')  # 输入平台订单号
        time.sleep(1)
        self.click_element(loc.seek_button, model='点击搜索按钮')  # 点击搜索按钮
        time.sleep(2)
        self.click_element(loc.order_caoz, model='勾选第一个订单')  # 勾选第一个订单
        time.sleep(1)
        self.click_element(loc.kdi_duop,model='移动到多仓库——多仓打单')     #移动到多仓库——多仓打单
        self.switchover_html(1)
        time.sleep(0.8)
        self.click_element(loc.choice, model='选择当前选择')  # 选择当前选择
        self.driver.switch_to.default_content()
        time.sleep(0.8)
        self.click_element(loc.ok_click, model='当前选择确认')  # 点击确认
        time.sleep(2)

    #多仓打单
    def dadna_move_suo_duocang(self,code):
        logging.info('多仓订单锁单')
        self.click_element(loa.start_guanli,model='点击收发货管理')                        #点击收发货管理
        self.click_element(loa.duocang_print,model='点击多仓打单')                     #点击快递—按货打单按钮
        time.sleep(2)
        # js = 'var q=document.documentElement.scrollTop=1000'
        # self.driver.execute_script(js)
        self.select(loa.order_code_shai,'平台订单号',model='筛选条件为平台订单号')           #筛选条件为平台订单号
        self.input_text(loa.order_shai_value,code,model='输入平台订单号')              #输入平台订单号
        time.sleep(1)
        self.click_element(loa.seek_button,model='点击查询按钮')                     #点击查询按钮
        time.sleep(2)
        js = 'var q=document.documentElement.scrollTop=10000'
        self.driver.execute_script(js)
        get_sku=str(self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU'))
        sku=get_sku.split('\n')
        self.click_element(loa.order_caoz,model='勾选当前订单')                      #选择当前订单
        time.sleep(0.5)
        self.click_element(loa.anhuo_suo_order,model='点击当前订单')                 #锁定订单
        time.sleep(0.5)
        self.switchover_html(2)
        self.click_element(loa.choice,model='点击当前选择')                          #当前选择
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.click_element(loa.ok_click,model='点击确认按钮')                        #确认按钮
        return str(sku[0])                                                        #返回SKU，用于扫描

    #权限的待合并----等待打单
    def qx_hb_move_daidadan(self,yunshu_genre):
        logging.info('权限验证（待合并----等待打单）')
        self.click_element(loc.order_caoz, model='订单选择')
        time.sleep(0.5)
        if yunshu_genre=="快递":
            self.select(loc.order_move,'快递-等待打单', model='移动至快递-等待打单')
            time.sleep(1)
            self.get_alert()
            time.sleep(1)
            self.click_element(loc.ok_click, model='提示语确认')
            time.sleep(2)
            return str(self.get_text(loc.order_status,model='返回订单状态'))
        elif yunshu_genre=="转运":
            self.select(loc.order_move,'转运-等待打单', model='移动至转运-等待打单')
            time.sleep(1)
            self.get_alert()
            time.sleep(1)
            self.click_element(loc.ok_click,model='提示语确认')
            time.sleep(2)
            return str(self.get_text(loc.order_status, model='返回订单状态'))
        else:
            self.select(loc.order_move,'等待打单', model='移动至等待打单')
            time.sleep(1)
            self.get_alert()
            time.sleep(1)
            self.click_element(loc.ok_click, model='提示语确认')
            time.sleep(2)
            return str(self.get_text(loc.order_status, model='返回订单状态'))

    # 权限的等待打单—打单
    def qx_dengdai_move_dadan(self, yunshu_mold,mold):

        logging.info('权限验证（等待打单—打单）')
        self.click_element(loc.order_caoz, model='勾选第一个订单')
        time.sleep(3)
        if yunshu_mold == "快递-等待打单":
            if  mold=="按货打单":
                self.select(loc.order_move, '快递-按货打单', model='移动至快递-按货打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '快递-核对打单', model='选择移动至快递-核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认按钮')
                else:
                    self.click_element(loc.ok_click, model='点击确认按钮')
                time.sleep(2)
            elif mold=="按框打单":
                self.select(loc.order_move, '快递-按筐打单', model='移动至快递-按框打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '快递-核对打单', model='移动至快递-核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            elif mold=="核对打单":
                self.select(loc.order_move, '快递-核对打单', model='移动至快递-核对打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            elif mold=="多品打单":
                self.select(loc.order_move, '快递-多品打单', model='移动至快递-多品打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '快递-核对打单', model='移动至快递-核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
        elif yunshu_mold == "转运-等待打单":
            if mold == "按货打单":
                self.select(loc.order_move, '转运-按货打单', model='移动至转运-按货打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH,'//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx,model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '转运-核对打单', model='移动至转运-核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            elif mold == "多品打单":
                self.select(loc.order_move, '转运-多品打单', model='移动至转运-多品打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '转运-核对打单', model='移动至转运-核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            else:
                self.select(loc.order_move, '转运-核对打单', model='移动至转运-核对打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)

        else:
            if mold == "按货打单":
                self.select(loc.order_move, '按货打单', model='移动至按货打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '核对打单', model='移动至核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            elif mold == "按框打单":
                self.select(loc.order_move, '按筐打单', model='移动至按筐打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '核对打单', model='移动至核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            elif mold == "核对打单":
                self.select(loc.order_move, '核对打单', model='移动至核对打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)
            elif mold == "多品打单":
                self.select(loc.order_move, '多品打单', model='移动至多品打单')
                time.sleep(1)
                self.get_alert()
                time.sleep(1)
                get_status_qx = (By.XPATH, '//*[@class="ui-dialog-body"]//div[@style]//div[@style]')
                if "操作失败" in self.get_text(get_status_qx, model="获取是否需要核对打单的文本"):
                    self.click_element(loc.ok_click, model='点击确认')
                    self.select(loc.order_move, '核对打单', model='移动至核对打单')
                    time.sleep(1)
                    self.get_alert()
                    time.sleep(1)
                    self.click_element(loc.ok_click, model='点击确认')
                else:
                    self.click_element(loc.ok_click, model='点击确认')
                time.sleep(2)


    #获取仓库信息
    get_cangku_text = (By.XPATH,'//*[@id="order-list"]//tr[2]//td[5]//dl')
    def get_cangku(self):
        sss=str(self.get_text(self.get_cangku_text,model='获取仓库信息'))
        s=sss.split('\n')
        return s[1]

    #订单状态
    order_status = (By.XPATH,'//*[@id="order-list"]//tbody//tr//td[3]//*')
    def get_status(self):
        status= str(self.get_text(self.order_status, model="获取订单状态"))
        time.sleep(1)
        return status


    def get_sku_qx(self):
        sku =self.get_text(loc.order_sku_qx,model="获取订单SKU")
        return sku

    #权限锁单操作
    def dadna_move_suo_qx(self,code,moth):
        logging.info('{0}到锁单'.format(moth))
        self.click_element(loa.start_guanli,model='点击收发货管理')                        #点击收发货管理
        if moth=="快递-按货打单":
            self.click_element(loa.kdi_anhuo_print,model='点击快递-按钮打单')                     #点击快递—按货打单按钮
            time.sleep(2)
            self.select(loa.order_code_shai,'平台订单号',model='筛选条件为平台订单号')           #筛选条件为平台订单号
            self.input_text(loa.order_shai_value,code,model='输入平台订单号')              #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button,model='点击查询按钮')                     #点击查询按钮
            time.sleep(2)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            self.click_element(loa.order_caoz,model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order,model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice,model='选择当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click,model='点击确认')                        #确认按钮
            get_sku=self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return   sku[0]      #返回SKU，用于扫描
        elif moth=="快递-按筐打单":
            self.click_element(loa.kdi_ankuang_print, model='点击快递-按钮打单')                   #点击快递—按框打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')          #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击查询按钮')                     #点击查询按钮
            time.sleep(2)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            self.click_element(loa.order_caoz, model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='选择当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='点击确认')                        #确认按钮
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return sku[0]  #返回SKU，用于扫描     #返回SKU，用于扫描
        elif moth=="快递-多品打单":
            self.click_element(loa.kdi_duopin_print, model='点击快递-多品打单')                     #点击快递—多品打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')            #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击查询按钮')                     #点击查询按钮

            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)

            time.sleep(2)
            self.click_element(loa.order_caoz, model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='选择当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='点击确认')                         #确认按钮
            get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return sku[0]  # 返回SKU，用于扫描
        elif moth == "转运-按货打单":
            self.click_element(loa.zyun_anhuo_print, model='点击转运-按货打单按钮')  # 点击快递—按货打单按钮
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')  # 筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')  # 输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击查询按钮')  # 点击查询按钮
            time.sleep(2)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            self.click_element(loa.order_caoz, model='选择当前订单')  # 选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')  # 锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='选择当前选择')  # 当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='点击确认')  # 确认按钮
            get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return sku[0]  # 返回SKU，用于扫描
        elif moth=="转运-多品打单":

            self.click_element(loa.zyun_duopin_print, model='点击转运-多品打单按钮')                     #点击快递—多品打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')            #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击查询按钮')                     #点击查询按钮

            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            if self.isElementExist((By.XPATH, '//*[@id="order-list"]//tbody//tr[2]//td[5]//div[2]'))!=True:
                cangku = self.get_text((By.XPATH, '//*[@id="order-list"]//tbody//tr[2]//td[5]//div[2]'), model="获取仓库文本")
                self.select((By.XPATH, '//*[@name="query.warehouseId"]'), cangku, model="选择仓库")
                time.sleep(2)
                self.click_element(loa.order_caoz, model='选择当前订单')                      #选择当前订单
                time.sleep(0.5)
                self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
                time.sleep(0.5)
                self.switchover_html(2)
                self.click_element(loa.choice, model='选择当前选择')                          #当前选择
                self.driver.switch_to.default_content()
                time.sleep(1)
                self.click_element(loa.ok_click, model='点击确认')                         #确认按钮
                get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
                sku = get_sku.split('\n')
                return sku[0]  # 返回SKU，用于扫描
            else:
                self.click_element((By.XPATH,'//*[@id="menu_13160000"]//*[@id="menu_13161700"]/a'), model='点击转运-多品打单按钮')  # 点击快递—多品打单
                time.sleep(2)
                self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')  # 筛选条件为平台订单号
                self.input_text(loa.order_shai_value, code, model='输入平台订单号')  # 输入平台订单号
                time.sleep(0.5)
                self.click_element(loa.seek_button, model='点击查询按钮')  # 点击查询按钮

                js = 'var q=document.documentElement.scrollTop=10000'
                self.driver.execute_script(js)
                cangku = self.get_text((By.XPATH, '//*[@id="order-list"]//tbody//tr[2]//td[5]//div[2]'), model="获取仓库文本")
                self.select((By.XPATH, '//*[@name="query.warehouseId"]'), cangku, model="选择仓库")
                time.sleep(2)
                self.click_element(loa.order_caoz, model='选择当前订单')  # 选择当前订单
                time.sleep(0.5)
                self.click_element(loa.anhuo_suo_order, model='锁定订单')  # 锁定订单
                time.sleep(0.5)
                self.switchover_html(2)
                self.click_element(loa.choice, model='选择当前选择')  # 当前选择
                self.driver.switch_to.default_content()
                time.sleep(1)
                self.click_element(loa.ok_click, model='点击确认')  # 确认按钮
                get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
                sku = get_sku.split('\n')
                return sku[0]  # 返回SKU，用于扫描
        elif moth=="按货打单":
            self.click_element(loa.anhuo_print,model='点击按货打单按钮')                     #点击快递—按货打单按钮
            time.sleep(2)
            self.select(loa.order_code_shai,'平台订单号',model='筛选条件为平台订单号')           #筛选条件为平台订单号
            self.input_text(loa.order_shai_value,code,model='输入平台订单号')              #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button,model='点击查询按钮')                     #点击查询按钮
            time.sleep(3)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            self.click_element(loa.order_caoz,model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order,model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice,model='选择当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click,model='点击确认')                        #确认按钮
            get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return sku[0]  # 返回SKU，用于扫描
        elif moth=="按筐打单":
            self.click_element(loa.ankuang_print, model='点击按框打单按钮')                   #点击快递—按框打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')          #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击查询按钮')                     #点击查询按钮
            time.sleep(3)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            self.click_element(loa.order_caoz, model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='选择当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='点击确认')                        #确认按钮
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return sku[0]  # 返回SKU，用于扫描
        elif moth=="多品打单":
            self.click_element(loa.duopin_print, model='点击多品打单按钮')                     #点击快递—多品打单
            time.sleep(2)
            self.select(loa.order_code_shai, '平台订单号', model='筛选条件为平台订单号')            #筛选条件为平台订单号
            self.input_text(loa.order_shai_value, code, model='输入平台订单号')             #输入平台订单号
            time.sleep(0.5)
            self.click_element(loa.seek_button, model='点击查询按钮')                     #点击查询按钮
            time.sleep(3)
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            cangku=self.get_text((By.XPATH,'//*[@id="order-list"]//tbody//tr[2]//td[5]//div[2]'),model="获取仓库文本")
            self.select((By.XPATH,'//*[@name="query.warehouseId"]'),cangku,model="选择仓库")
            time.sleep(0.5)
            self.click_element(loa.order_caoz, model='选择当前订单')                      #选择当前订单
            time.sleep(0.5)
            self.click_element(loa.anhuo_suo_order, model='锁定订单')                 #锁定订单
            time.sleep(0.5)
            self.switchover_html(2)
            self.click_element(loa.choice, model='选择当前选择')                          #当前选择
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.click_element(loa.ok_click, model='点击确认')                         #确认按钮
            js = 'var q=document.documentElement.scrollTop=10000'
            self.driver.execute_script(js)
            get_sku = self.get_text((By.XPATH, '//*[@id="order-list"]//tr[2]//td[5]'), model='SKU')
            sku = get_sku.split('\n')
            return sku[0]  # 返回SKU，用于扫描

        else:
            print("输入错误")
    #
    scan_mold = (By.XPATH,'//*[@id="order-list"]//tbody//tr[1]//td[3]//span[1]')
    def get_scan_mold(self):
        return self.get_text(self.scan_mold,model="获取扫描的方式")
