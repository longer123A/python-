#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from selenium.webdriver.common.by import By
from python_ERP.PageLocators.order_mana_guanli import OrderMana as loc
from python_ERP.Common.BasePage import BasePage
import time
from python_ERP.Common import logger
import logging
from python_ERP.Common.logger import *
from python_ERP.TestDatas.chuh_scan_data import wuli_data
import re
from python_ERP.TestDatas.baog_Data import dict_data

class OrderPage(BasePage):


    #点击新建订单按钮
    def new_order(self):
        logging.info("点击新建订单按钮")
        self.click_element(loc.order_button,model='点击新建按钮')
        self.window_switch_order(-1)
        time.sleep(2)

    #待检查—待合并
    def jian_move_he(self,code):
        time.sleep(3)
        logging.info('待检查转为待合并')
        self.click_element(loc.order_caoz,model='勾选第一个订单')           #选择第一个订单
        time.sleep(0.5)
        self.click_element(loc.dingdan_move,model='订单移动操作栏')         #订单移动操作栏
        time.sleep(0.5)
        self.click_element(loc.wait_he,model='点击一键等待打单')              #点击等待打单
        self.get_alert(model='弹窗处理')                              #
        time.sleep(1)
        self.click_element(loc.ok_button,model='点击OK按钮')            #点击OK按钮
        time.sleep(2)
        self.chaxun_code(code)                                  #查询订单号及查询唯一

    def jian_move_he_qx(self,code):
        self.chaxun_code(code)  # 查询订单号及查询唯一
        time.sleep(3)
        logging.info('待检查转为待合并')
        self.click_element(loc.order_caoz,model='勾选第一个订单')           #选择第一个订单
        time.sleep(0.5)
        self.click_element(loc.dingdan_move,model='订单移动操作栏')         #订单移动操作栏
        time.sleep(0.5)
        self.click_element(loc.wait_he,model='点击一键等待打单')              #点击等待打单
        self.get_alert(model='弹窗处理')                              #弹窗处理
        time.sleep(1)
        self.click_element(loc.ok_button,model='点击OK按钮')            #点击OK按钮
        time.sleep(2)


    #查询订单号
    def chaxun_code(self,code):
        logging.info('查询订单号')
        self.input_text(loc.chaxun_code,code,model='输入平台订单号')
        self.click_element(loc.code_button,model='点击搜索按钮')
        time.sleep(3)

    #运输方式选择
    def freight_gu(self,moth):
        logging.info('运费估算')
        self.click_element(loc.freight_gu,model='点击运费估算')
        self.switchover_html(1)
        time.sleep(0.5)


        if  moth=="快递" or moth=="多仓":
            self.select(loc.yunshu_mode, '快递', model='选择快递类型')
            self.click_element(loc.kdi_sousuo, model='点击搜索按钮')
            time.sleep(1)
            try:

                if self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'),model='获取第一个快递文本') in wuli_data:
                    xinxi =self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'),model='获取第一个快递文本')
                    logging.info("物流方式：{0}".format(xinxi))
                    return wuli_data.index(xinxi)
                elif self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[2]/td[2]'), model='获取第二个快递文本') in wuli_data:
                    xinxi = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'),model='获取第二个快递文本')
                    logging.info("物流方式：{0}".format(xinxi))
                    return wuli_data.index(xinxi)
                elif self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[3]/td[2]'), model='获取第三个快递文本') in wuli_data:
                    xinxi = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'),model='获取第三个快递文本')
                    logging.info("物流方式：{0}".format(xinxi))
                    return wuli_data.index(xinxi)
                elif self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[4]/td[2]'), model='获取第四个快递文本') in wuli_data:
                    xinxi = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'),model='获取第四个快递文本')
                    logging.info("物流方式：{0}".format(xinxi))
                    return wuli_data.index(xinxi)
                elif self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[5]/td[2]'), model='获取第五个快递文本') in wuli_data:
                    xinxi = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'),model='获取第五个快递文本')
                    logging.info("物流方式：{0}".format(xinxi))
                    return wuli_data.index(xinxi)
                else:
                    pass
            except:
                return '无快递'
            finally:
                self.driver.switch_to.default_content()
                time.sleep(1)
                self.click_element(loc.ok_button, model='确认')
        else:
            #~~~~~~~~~~~~~~~测试平邮用，测试完毕需要删除~~~~~~~~~
            # self.select(loc.yunshu_mode, '平邮', model=nama)
            # self.click_element(loc.kdi_sousuo, model=nama)
            # time.sleep(1)

            time.sleep(1)
            xinxi = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]'), model='获取第一个运输文本')

            xinxi2 = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[2]/td[2]'), model='获取第二个运输文本')
            xinxi3 = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[3]/td[2]'), model='获取第三个运输文本')
            xinxi4 = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[4]/td[2]'), model='获取第四个运输文本')
            xinxi5 = self.get_text((By.XPATH, '//*[@id="data-list"]/tbody/tr[5]/td[2]'), model='获取第五个运输文本')
            try:
                if xinxi in wuli_data:
                    # xinxi = (By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]')
                    logging.info("物流方式：{0}".format(wuli_data.index(xinxi)))
                    return wuli_data.index(xinxi)
                elif xinxi2 in wuli_data:
                    # xinxi = (By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]')
                    logging.info("物流方式：{0}".format(wuli_data.index(xinxi2)))
                    return wuli_data.index(xinxi2)

                elif xinxi3 in wuli_data:
                    # xinxi = (By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]')
                    logging.info("物流方式：{0}".format(wuli_data.index(xinxi3)))
                    return wuli_data.index(xinxi3)
                elif xinxi4 in wuli_data:
                    # xinxi = (By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]')
                    logging.info("物流方式：{0}".format(wuli_data.index(xinxi4)))
                    return wuli_data.index(xinxi4)
                elif xinxi5 in wuli_data:
                    # xinxi = (By.XPATH, '//*[@id="data-list"]/tbody/tr[1]/td[2]')
                    logging.info("物流方式：{0}".format(wuli_data.index(xinxi5)))
                    return wuli_data.index(xinxi5)
            except:
                return '无快递'
            finally:
                self.driver.switch_to.default_content()
                time.sleep(1)
                self.click_element(loc.ok_button, model='确认')

    #修改快递方式
    def xiu_kdi_moth(self,moth,code):
        time.sleep(0.5)
        logging.info('修改快递方式')
        self.click_element(loc.order_caoz,model='修改第一个订单')
        time.sleep(0.5)
        self.click_element(loc.kdi_moth,model='修改运输方式')
        self.input_text(loc.input_moth,moth,model='输入运输方式')
        time.sleep(0.3)
        self.click_element(loc.click_moth,model='点击运输方式')
        self.get_alert()
        time.sleep(1)
        self.click_element(loc.ok_button,model='确认')

        #订单号
        dingdan_code = self.get_text(loc.order_caoz)

        time.sleep(1)
        self.click_element(loc.order_xiug,model='修改订单')
        self.window_switch_order(-1)
        time.sleep(2)
        # self.wait_eleVisible(loc.order_geng,model='查找跟踪号元素')
        self.input_text(loc.order_geng,code,model='输入跟踪号')
        time.sleep(1)
        self.click_element(loc.gen_code_od,model='增加跟踪号')
        return dingdan_code


    #修改运输方式

    def xiu_kdi_moth_qx(self,moth,code):
        time.sleep(0.5)
        logging.info('修改快递方式')
        self.click_element(loc.order_caoz,model='修改第一个订单')
        time.sleep(0.5)
        self.click_element(loc.yunshu_moth,model='修改运输方式')
        self.input_text(loc.input_moth_qx,moth,model='输入运输方式')
        time.sleep(0.3)
        self.click_element(loc.click_moth_qx,model='点击运输方式')
        self.get_alert()
        time.sleep(1)
        self.click_element(loc.ok_button,model='确认')

        #订单号
        dingdan_code = self.get_text(loc.order_caoz)

        time.sleep(1)
        self.click_element(loc.order_xiug,model='修改订单')
        self.window_switch_order(-1)
        time.sleep(2)
        # self.wait_eleVisible(loc.order_geng,model='查找跟踪号元素')
        self.input_text(loc.order_geng,code,model='输入跟踪号')
        time.sleep(1)
        self.click_element(loc.gen_code_od,model='增加跟踪号')
        time.sleep(3)
        return dingdan_code


    #判断订单状态
    def get_order_statu(self,dingdan_code):
        logging.info('判断订单状态')
        self.input_text(loc.sousuo_order,dingdan_code,model='输入订单号')
        time.sleep(0.5)
        self.click_element(loc.sousuo_button,model='点击搜索按钮')
        time.sleep(2)
        return str(self.get_text(loc.order_statu,model='获取订单状态'))


    #修改运输成本
    def xiugai_money(self):
        logging.info("修改实际运费")
        s=str(self.get_text(loc.order_money,model='获取运输成本'))
        s2=s.split('\n')
        ss=s2[2][5:-4]
        time.sleep(1)
        self.click_element(loc.order_caoz,model='勾选第一个订单')
        time.sleep(0.5)
        self.select(loc.order_caozou,'批量修改运费成本',model='选择批量修改运费成本')
        self.switchover_html(1)
        time.sleep(1)
        self.input_text(loc.xin_yunfei,ss,model='输入运输成本')
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.click_element(loc.ok_button,model='点击确认按钮')
        time.sleep(3)

    #窗口切换
    def window_switch_order(self,index):
        self.window_switch(index,model= '窗口切换')

    #
    def get_scan_wuliumold(self,get_moth_index):
        # dict_data
        for get_wuliumoth in dict_data:
            if get_moth_index in list(get_wuliumoth.values())[0]:
                return list(get_wuliumoth.keys())[0]
            else:
                # return str(get_moth_index).split("(" and ")")
                s = get_moth_index.split("(")
                sss = s[1].split(")")
                return sss
