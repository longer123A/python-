#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xu
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from python_ERP.Common.BasePage import BasePage
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from python_ERP.Common import logger
import logging
import pyautogui

class KdiScan(BasePage):
    #收发货管理
    start_guanli = (By.XPATH,'//*[@id="menu_13000000"]')
    #快递按货扫描
    kdi_scan_anhuo = (By.XPATH,'//*[@id="menu_13113700"]/a')
    #sku
    sku = (By.XPATH,'//*[@id="sku"]')

    #快递按货扫描
    def kdi_scan_anh(self,sku):
        logging.info('快递按货扫描')
        self.click_element(self.start_guanli,model='点击收发货管理')            #点击收发货管理
        self.click_element(self.kdi_scan_anhuo,model='点击快递按钮扫描')          #点击快递按货扫描
        time.sleep(2)
        self.input_text(self.sku,sku,model='输入sku')                    #输入sku
        self.get_element(self.sku).send_keys(Keys.ENTER)
        time.sleep(20)                                              #程序反应较慢



    #出库扫描
    cku_scan = (By.XPATH,'//*[@id="menu_13111100"]/a')

    #快递方式click
    kdi_click = (By.XPATH,'//*[@id="s2id_logistics-type"]')
    #快递方式input
    kdi_input = (By.XPATH,'//*[@id="s2id_autogen1_search"]')
    #选择快递
    kdi_choine = (By.XPATH,'//*[@id="select2-drop"]//ul')

    #输入跟踪号
    kdi_code = (By.XPATH,'//*[@id="trackingnum"]')

    #重量输入
    weight_input = (By.XPATH,'//*[@placeholder="请输入数字"]')

    #强制出库
    force_cku = (By.XPATH,'//*[@data-id="ok"]')

    #快递出库扫描
    def kdi_scan_cku(self,moth,code):
        logging.info('快递出库扫描')
        self.driver.refresh()
        time.sleep(1)
        self.click_element(self.start_guanli,model='点击收发货管理')               #点击收发货管理
        time.sleep(0.5)
        self.click_element(self.cku_scan,model='点击快递出库扫描')                   #点击出库扫描

        time.sleep(25)
        self.click_element(self.kdi_click,model='快递列表点击')                  #快递列表点击
        time.sleep(0.5)
        self.input_text(self.kdi_input,moth,model='快递列表输入')                #快递列表输入
        time.sleep(0.5)
        self.click_element(self.kdi_choine,model='快递列表选择')                 #快递列表选择
        time.sleep(1)
        self.input_text(self.kdi_code,code,model='输入跟踪号')                 #输入跟踪号
        self.get_element(self.kdi_code).send_keys(Keys.ENTER)
        time.sleep(3)
        if self.isElementExist('//*[@placeholder="请输入数字"]')==True:
            self.input_text(self.weight_input,'0.1',model='输入重量')            #重量输入
            time.sleep(0.5)
        else:
            pass
        self.click_element(self.force_cku,model='点击强制出库按钮')                  #强制出库按钮
        time.sleep(2)



    #收发货管理

    # 快递按框扫描
    kdi_scan_ankuang = (By.XPATH,'//*[@id="menu_13000000"]//li[@id="menu_13113800"]')
    #sku1//*[@id="sku"]
    sku1 = (By.XPATH,'//*[@id="orderid"]')

    sku2 = (By.XPATH,'//*[@id="sku"]')
    def kdi_scan_ank(self,sku):
        logging.info('快递按框扫描')
        self.click_element(self.start_guanli, model='点击收发货管理')               #点击收发货管理
        self.click_element(self.kdi_scan_ankuang, model='点击快递按框扫描')           #点击快递按框扫描
        time.sleep(2)
        self.input_text(self.sku1, sku, model='输入sku')                     #输入sku
        time.sleep(1)
        self.get_element(self.sku1).send_keys(Keys.ENTER)
        time.sleep(1)
        self.input_text(self.sku2, sku, model='输入sku2')                     #输入sku2
        time.sleep(1)
        self.get_element(self.sku2).send_keys(Keys.ENTER)
        time.sleep(20)


    #获取多品打单批次号
    kdi_pici_code = (By.XPATH,'//*[@id="menu_13000000"]//*[@id="menu_13161300"]')
    pici_code = (By.XPATH,'//*[@id="menu_13160000"]//*[@id="menu_13161100"]')
    zyun_pici_code = (By.XPATH, '//*[@id="menu_13000000"]//*[@id="menu_13161600"]')
    #订单号筛选
    dingdan_code = (By.XPATH,'//*[@id="order-ids"]')
    #搜索按钮
    seek_button = (By.XPATH,'//*[@id="search-form"]//button[1]')
    #批次哈
    get_code = (By.XPATH,'//*[@id="order-list"]//tbody//tr[1]//td[1]//label')
    def get_picihao(self,dingdan_code,mold):
        logging.info('获取多品打单批次号')
        self.click_element(self.start_guanli, model='点击收发货管理')                #点击收发货管理
        if mold=="快递-多品打单":
            self.click_element(self.kdi_pici_code,model='点击多品批次号(快递单仓)')                    #点击多品批次号（快递单仓）
        elif mold=="转运-多品打单":
            self.click_element(self.zyun_pici_code, model='点击多品批次号(转运)')
        else:
            self.click_element(self.pici_code, model='点击多品批次号')
        time.sleep(3)
        self.input_text(self.dingdan_code,dingdan_code,model='输入订单号')       #输入订单号
        time.sleep(0.5)
        self.click_element(self.seek_button,model='点击搜索按钮')                   #点击搜索按钮
        time.sleep(2)
        return  self.get_text(self.get_code,model='返回订单号')                  #返回订单号




    #多品按货扫描—快递
    kdi_duopin_scan = (By.XPATH,'//*[@id="menu_13000000"]//*[@id="menu_13113300"]')

    #批次号
    picihao_code = (By.XPATH,'//*[@id="serialNumber"]')
    #sku
    input_sku = (By.XPATH,'//*[@id="sersku"]')
    #获取剩余sku
    get_sku = (By.XPATH,"//*[@id='order-grid-1']//tbody")
    #qr
    get_qr = (By.XPATH,'//*[@id="scan-record"]')

    def duopin_scan_kdi(self,dingdan_code,sku):
        logging.info('多品按货扫描—快递')
        self.click_element(self.start_guanli, model='点击收发货管理')                 #点击收发货管理
        self.click_element(self.kdi_duopin_scan, model='点击快递多品扫描按钮')                  #点击快递多品扫描按钮
        time.sleep(2)
        self.input_text(self.picihao_code,dingdan_code,model='输入订单号')        #输入订单号
        time.sleep(1)
        # self.get_element(self.picihao_code).send_keys(Keys.ENTER)
        time.sleep(1)
        self.input_text(self.input_sku, sku, model='输入sku')                  #输入sku
        time.sleep(1)

        s = self.get_text(self.get_sku,model='获取剩余sku')
        ss = s.split(' ')
        logging.info('sku2:{0}'.format(ss[0]))                            #获取剩余的sku

        time.sleep(1)
        self.input_text(self.input_sku, ss[0], model='输入剩余sku')                #输入剩余的sku
        time.sleep(1)
        self.get_element(self.input_sku).send_keys(Keys.ENTER)
        get_qr = self.get_text(self.get_qr,model='获取二维码信息')
        # logging.info('get_qr:{0}'.format(get_qr))
        qr = get_qr.split('\n')
        # logging.info('qr1:{0}'.format(qr))
        logging.info('qr2:{0}'.format(qr[0]))
        time.sleep(1)
        return qr[0]                                              #返回二维码序列号

    # 多品核对扫描
    kdi_hedui_button = (By.XPATH, '//ul[@class="nav nav-tabs custom"]//li[@id="menu_13113400"]')

    #多品核对打单剩余SKU
    get_hedui_sku = (By.XPATH,'//*[@id="check_scan_datas"]//td[@class="check_sku"]')
    def duo_scan_hedui(self,qr):
        logging.info('多品按货扫描—快递')
        self.click_element(self.kdi_hedui_button,model='多品核对扫描（快递）')           #多品核对扫描（快递）
        time.sleep(2)
        self.input_text(self.sku1,qr,model='输入二维码序号')                       #输入二维码序号
        time.sleep(1)
        self.get_element(self.sku1).send_keys(Keys.ENTER)
        time.sleep(1)
        get_sku = self.get_text(self.get_hedui_sku,model='获取sku')         #获取sku
        self.input_text(self.sku2,get_sku,model='输入sku')                  #输入sku
        time.sleep(1)
        self.get_element(self.sku2).send_keys(Keys.ENTER)
        time.sleep(10)

    #核对扫描
    kdi_hedui_scan = (By.XPATH,'//*[@id="menu_13110000"]//*[@id="menu_13111000"]')
    def hedui_scan(self,dingdan_code):
        logging.info('核对扫描')
        self.click_element(self.start_guanli, model='点击收发货管理')             #点击收发货管理
        time.sleep(0.5)
        self.click_element(self.kdi_hedui_scan,model='点击核对扫描按钮')         #点击核对扫描按钮
        time.sleep(2)
        self.input_text(self.sku1, dingdan_code, model='输入序列号')          #输入序列号
        time.sleep(1)
        self.get_element(self.sku1).send_keys(Keys.ENTER)
        time.sleep(1)
        sku=self.get_text((By.XPATH,'//*[@class="check_sku"]'),model='获取sku')
        self.input_text(self.sku,sku,model='输入sku')                      #输入sku
        self.get_element(self.sku).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.close()
        self.window_switch(-1)#由于环境原因，显示页面错误，但实际已扫描成功
        time.sleep(5)

    #多仓库批次号
    duocang_pici = (By.XPATH,'//*[@id="menu_13000000"]//*[@id="menu_13191100"]')
    #多仓库批次号
    def get_picihao_cuocang(self,dingdan_code):
        logging.info('多仓获取批次号快递')
        self.click_element(self.start_guanli, model='点击收发货管理')                #点击收发货管理
        self.click_element(self.duocang_pici,model='点击多品批次号（多仓）')                    #点击多品批次号（快递单仓）
        time.sleep(3)
        self.input_text(self.dingdan_code,dingdan_code,model='输入订单号')       #输入订单号
        time.sleep(0.5)
        self.click_element(self.seek_button,model='点击搜索按钮')                   #点击搜索按钮
        time.sleep(3)
        return  self.get_text(self.get_code,model='返回订单号')                  #返回订单号

    #多仓库按货扫描
    duocangku_anh_snca = (By.XPATH,'//*[@class="row"]//*[@id="menu_13113000"]/a')

    #序列号输入
    input_xulhao_duocang = (By.XPATH,'//*[@id="orderid"]')

    #sku输入
    input_sku_duocang = (By.XPATH,'//*[@id="sku"]')
    # 获取剩余SKU
    get_duocang_sku = (By.XPATH, "//*[@id='order-grid-1']//tbody")
    #多仓按货扫描
    def duopin_scan_duocang(self,dingdan_code,sku):
        logging.info('多仓按货扫描')
        self.click_element(self.start_guanli, model='点击收发货管理')                 #点击收发货管理
        self.click_element(self.kdi_hedui_scan, model='快递核对扫描')
        time.sleep(2)
        self.click_element(self.duocangku_anh_snca, model='快递多品扫描按钮')                  #点击快递多品扫描按钮
        time.sleep(2)
        self.input_text(self.input_xulhao_duocang,dingdan_code,model='输入订单号')        #输入订单号
        # self.get_element(self.input_xulhao_duocang).send_keys(Keys.ENTER)
        time.sleep(1)
        self.input_text(self.input_sku_duocang, sku, model='输入SKU')                  #输入sku
        time.sleep(1)
        self.get_element(self.input_sku_duocang).send_keys(Keys.ENTER)
        time.sleep(1)
        s = self.get_text(self.get_duocang_sku, model='获取剩余SKU')
        ss = s.split(' ')
        logging.info('sku2:{0}'.format(ss[0]))  # 获取剩余的sku

        time.sleep(1)
        self.input_text(self.input_sku_duocang, ss[0], model='输入剩余的sku')  # 输入剩余的sku
        time.sleep(1)
        self.get_element(self.input_sku_duocang).send_keys(Keys.ENTER)
        get_qr = self.get_text(self.get_qr, model='获取二维码信息')
        qr = get_qr.split('\n')
        # ss = s.split('')
        logging.info('qr2:{0}'.format(qr[0]))
        time.sleep(1)
        return qr[0]  # 返回二维码序列号

    #多仓核对扫描
    hedui_duocang_botton = (By.XPATH,'//*[@class="row"]//*[@id="menu_13113100"]')
    def hedui_scan_duocang(self,dingdan_code):
        logging.info('多仓核对扫描')
        self.click_element(self.hedui_duocang_botton,model='点击核对扫描按钮')         #点击核对扫描按钮
        time.sleep(2)
        self.input_text(self.sku1, dingdan_code, model='输入序列号')          #输入序列号
        time.sleep(1)
        self.get_element(self.sku1).send_keys(Keys.ENTER)
        time.sleep(1)
        sku=self.get_text((By.XPATH,'//*[@class="check_sku"]'),model='获取sku')
        self.input_text(self.sku,sku,model='输入sku')                      #输入sku
        self.get_element(self.sku).send_keys(Keys.ENTER)
        time.sleep(5)


    #按货扫描
    anh_scan = (By.XPATH,'//*[@id="menu_13111400"]/a')
    #按框扫描
    ank_scan = (By.XPATH,'//*[@id="menu_12161800"]/a')

    #多品扫描
    duop_scan = (By.XPATH, '//*[@id="menu_13101900"]/a')
    duop_scan_pyou= (By.XPATH,'//*[@id="menu_13110000"]//*[@id="menu_13112100"]')
    #核对扫描
    hedui_scan_ping = (By.XPATH,'//*[@id="menu_13111000"]/a')
    #转运按货扫描
    zyun_anh_scan  = (By.XPATH,'//*[@id="menu_13112700"]/a')
    #转运多品按货扫描
    zyun_duop_scan = (By.XPATH,'//*[@id="menu_13110000"]//*[@id="menu_13114100"]')
    #转运多品核对扫描
    zyun_duop_hedui_scan = (By.XPATH,'//*[@class="nav nav-tabs custom"]//*[@id="menu_13114200"]/a')
    #获取是否为按框打单
    get_ank = (By.XPATH,'//*[@class="success"]//td[5]//input')
    #
    #权限扫描所有方法
    def qx_scan(self,dingdan_code,sku,mold):
        logging.info("{0}开始扫描".format(mold))
        if mold=="按货打单":
            self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
            time.sleep(0.5)
            self.click_element(self.anh_scan, model='点击按货扫描')      # 点击按货扫描
            time.sleep(2)
            self.input_text(self.sku, sku, model='输入SKU')  # 输入sku
            self.get_element(self.sku).send_keys(Keys.ENTER)
            time.sleep(20)
        elif mold=="按筐打单":
            self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
            time.sleep(0.5)
            self.click_element((By.XPATH,'//*[@id="menu_13112500"]/a'), model='点击按框扫描')  # 点击快递按框扫描
            time.sleep(2)
            self.input_text(self.sku1, sku, model='输入SKU')  # 输入sku
            time.sleep(1)
            self.get_element(self.sku1).send_keys(Keys.ENTER)
            time.sleep(1)
            self.input_text(self.sku2, sku, model='输入SKU2')  # 输入sku2
            time.sleep(1)
            self.get_element(self.sku2).send_keys(Keys.ENTER)
            time.sleep(20)
        elif mold=="多品打单":
            #获取批次号
            picihao_code=self.get_picihao(dingdan_code,mold)
            time.sleep(2)
            #~~~~~~~~~~~~~多品扫描~~~~~~~~~~~~
            self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
            time.sleep(0.5)
            self.click_element(self.duop_scan_pyou, model='点击多品打单')  # 点击快递多品扫描按钮
            time.sleep(2)
            self.input_text(self.picihao_code, picihao_code, model='输入批次号')  # 输入批次号
            self.get_element(self.picihao_code).send_keys(Keys.ENTER)
            time.sleep(1)
            self.input_text(self.input_sku, sku, model='输入SKU')  # 输入sku
            self.get_element(self.input_sku).send_keys(Keys.ENTER)
            time.sleep(1)
            s = self.get_text(self.get_sku, model='获取剩余SKU')
            ss = s.split(' ')
            logging.info('sku2:{0}'.format(ss[0]))  # 获取剩余的sku

            time.sleep(1)
            self.input_text(self.input_sku, ss[0], model='输入剩余SKU')  # 输入剩余的sku
            time.sleep(1)
            self.get_element(self.input_sku).send_keys(Keys.ENTER)
            get_qr = self.get_text(self.get_qr, model='获取二维码信息')
            split_qr = get_qr.split('\n')
            logging.info('qr2:{0}'.format(split_qr[0]))
            time.sleep(1)
            qr=split_qr[0]  # 返回二维码序列号

            #多品核对扫描
            self.click_element((By.XPATH,'//*[@class="nav nav-tabs custom"]//*[@id="menu_13112200"]'), model='点击多品核对扫描')  # 多品核对扫描（快递）
            time.sleep(2)
            self.input_text(self.sku1, qr, model='输入二维码信息')  # 输入二维码序号
            time.sleep(1)
            self.get_element(self.sku1).send_keys(Keys.ENTER)
            time.sleep(1)
            get_sku = self.get_text(self.get_hedui_sku, model='获取SKU')  # 获取sku
            self.input_text(self.sku2, get_sku, model='输入SKU')  # 输入sku
            time.sleep(1)
            self.get_element(self.sku2).send_keys(Keys.ENTER)
            time.sleep(10)
        elif mold=="核对打单":
            try:
                self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
                time.sleep(0.5)
                self.click_element(self.hedui_scan_ping, model='点击核对打单')  # 点击核对扫描按钮
                time.sleep(2)
                self.input_text(self.sku1, dingdan_code, model='输入序列号')  # 输入序列号
                self.get_element(self.sku1).send_keys(Keys.ENTER)
                time.sleep(1)
                if self.isElementExist(self.get_ank)==True:
                    if self.get_element_attribute(self.get_ank,"value",model="获取是否为单品多件产品")=="0":
                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取sku')
                        self.input_text(self.sku, sku, model='输入sku')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        self.input_text(self.sku, sku, model='输入sku2')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
                    else:

                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取sku')
                        self.input_text(self.sku, sku, model='输入sku')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
                else:
                    shu=(By.XPATH,'//*[@class="check_quantity"]')
                    if self.get_text(shu,model="获取需要扫描的数量")==1:
                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取sku')
                        self.input_text(self.sku, sku, model='输入sku')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
                    else:
                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取sku')
                        self.input_text(self.sku, sku, model='输入sku')  # 输入sku
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        self.input_text(self.sku, sku, model='输入sku2')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
            except:
                self.driver.close()
                self.window_switch(-1)
                time.sleep(2)
            finally:
                self.driver.close()
                self.window_switch(-1)
                time.sleep(2)

        #~~~~~~~~~~~~快递扫描~~~~~~~~~~~
        elif mold=="快递-按货打单":
            self.kdi_scan_anh(sku)
        elif mold=="快递-按筐打单":
            self.kdi_scan_ank(sku)
        elif mold=="快递-多品打单":
            picihao_code = self.get_picihao(dingdan_code,mold)
            qr = self.duopin_scan_kdi(picihao_code, sku)
            self.duo_scan_hedui(qr)
        elif mold=="快递-核对打单":
            self.hedui_scan(dingdan_code)

        #~~~~~~~~~~~~转运扫描~~~~~~~~~~
        elif mold=="转运-按货打单":
            self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
            self.click_element(self.zyun_anh_scan, model='点击转运按货扫描')      # 点击按货扫描
            time.sleep(2)
            self.input_text(self.sku, sku, model='输入sku')  # 输入sku
            self.get_element(self.sku).send_keys(Keys.ENTER)
            time.sleep(20)
        elif mold=="转运-多品打单":
            #获取批次号
            picihao_code=self.get_picihao(dingdan_code,mold)
            time.sleep(2)
            #~~~~~~~~~~~~~多品扫描~~~~~~~~~~~~
            self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
            # self.click_element(self.anh_scan, model=nama)  # 点击多品扫描按钮
            # time.sleep(2)
            self.click_element(self.zyun_duop_scan,model='点击转运-多品打单')
            time.sleep(2)
            self.input_text(self.picihao_code, picihao_code, model='输入序列号')  # 输入批次号
            self.get_element(self.picihao_code).send_keys(Keys.ENTER)
            time.sleep(1)
            self.input_text(self.input_sku, sku, model='输入sku')  # 输入sku
            self.get_element(self.input_sku).send_keys(Keys.ENTER)
            time.sleep(1)
            s = self.get_text(self.get_sku, model='获取剩余SKU')
            ss = s.split(' ')
            logging.info('sku2:{0}'.format(ss[0]))  # 获取剩余的sku

            time.sleep(1)
            self.input_text(self.input_sku, ss[0], model='输入剩余SKU')  # 输入剩余的sku
            time.sleep(1)
            self.get_element(self.input_sku).send_keys(Keys.ENTER)
            get_qr = self.get_text(self.get_qr, model='获取二维码信息')
            split_qr = get_qr.split('\n')
            logging.info('qr2:{0}'.format(split_qr[0]))
            time.sleep(1)
            qr=split_qr[0]  # 返回二维码序列号

            #多品核对扫描
            self.click_element(self.zyun_duop_hedui_scan, model='点击转运多品核对扫描')  # 多品核对扫描（快递）
            time.sleep(2)
            self.input_text(self.sku1, qr, model='输入二维码')  # 输入二维码序号
            time.sleep(1)
            self.get_element(self.sku1).send_keys(Keys.ENTER)
            time.sleep(1)
            get_sku = self.get_text(self.get_hedui_sku, model='获取sku')  # 获取sku
            self.input_text(self.sku2, get_sku, model='输入SKU')  # 输入sku
            time.sleep(1)
            self.get_element(self.sku2).send_keys(Keys.ENTER)
            time.sleep(10)
        elif mold=="转运-核对打单":
            self.click_element(self.start_guanli, model='点击收发货管理')  # 点击收发货管理
            time.sleep(0.5)
            self.click_element(self.hedui_scan_ping, model='点击转运-核对打单')  # 点击核对扫描按钮
            time.sleep(2)
            self.input_text(self.sku1, dingdan_code, model='输入订单号')  # 输入订单号
            time.sleep(1)
            self.get_element(self.sku1).send_keys(Keys.ENTER)
            try:
                if self.isElementExist(self.get_ank)==True:
                    if self.get_element_attribute(self.get_ank,"value",model="获取是否为单品多件产品")=="0":
                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取SKU')
                        self.input_text(self.sku, sku, model='输入SKU')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        self.input_text(self.sku, sku, model='输入SKU2')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
                    else:

                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取SKU')
                        self.input_text(self.sku, sku, model='输入SKU')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
                else:
                    shu=(By.XPATH,'//*[@class="check_quantity"]')
                    if self.get_text(shu,model="获取需要扫描的数量")==1:
                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取SKU')
                        self.input_text(self.sku, sku, model='输入SKU')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
                    else:
                        time.sleep(1)
                        sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model='获取SKU')
                        self.input_text(self.sku, sku, model='输入SKU')  # 输入sku
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        self.input_text(self.sku, sku, model='输入SKU2')  # 输入sku
                        time.sleep(1)
                        self.get_element(self.sku).send_keys(Keys.ENTER)
                        time.sleep(1)
                        # self.driver.switch_to_alert().accept()
                        time.sleep(5)
            except:
                self.driver.close()
                self.window_switch(-1)
                time.sleep(2)
            finally:
                self.driver.close()
                self.window_switch(-1)
                time.sleep(2)
            # if self.isElementExist(self.get_ank)==True:
            #     if self.get_element_attribute(self.get_ank,"value",model="获取是否为单品多件产品")=="0":
            #         time.sleep(1)
            #         sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model=nama)
            #         self.input_text(self.sku, sku, model=nama)  # 输入sku
            #         time.sleep(1)
            #         self.get_element(self.sku).send_keys(Keys.ENTER)
            #         time.sleep(1)
            #         self.input_text(self.sku, sku, model=nama)  # 输入sku
            #         time.sleep(1)
            #         self.get_element(self.sku).send_keys(Keys.ENTER)
            #         time.sleep(1)
            #         self.driver.refresh()  # 由于环境原因，显示页面错误，但实际已扫描成功
            #         time.sleep(5)
            #     else:
            #
            #         time.sleep(1)
            #         sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model=nama)
            #         self.input_text(self.sku, sku, model=nama)  # 输入sku
            #         self.get_element(self.sku).send_keys(Keys.ENTER)
            #         time.sleep(1)
            #         self.driver.refresh()  # 由于环境原因，显示页面错误，但实际已扫描成功
            #         time.sleep(5)
            # else:
            #     shu=(By.XPATH,'//*[@class="check_quantity"]')
            #     if self.get_text(shu,model="获取需要扫描的数量")==1:
            #         time.sleep(1)
            #         sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model=nama)
            #         self.input_text(self.sku, sku, model=nama)  # 输入sku
            #         self.get_element(self.sku).send_keys(Keys.ENTER)
            #         time.sleep(1)
            #         self.driver.refresh()  # 由于环境原因，显示页面错误，但实际已扫描成功
            #         time.sleep(5)
            #     else:
            #         time.sleep(1)
            #         sku = self.get_text((By.XPATH, '//*[@class="check_sku"]'), model=nama)
            #         self.input_text(self.sku, sku, model=nama)  # 输入sku
            #         self.get_element(self.sku).send_keys(Keys.ENTER)
            #         time.sleep(1)
            #         self.input_text(self.sku, sku, model=nama)  # 输入sku
            #         self.get_element(self.sku).send_keys(Keys.ENTER)
            #         time.sleep(1)
            #         self.driver.refresh()  # 由于环境原因，显示页面错误，但实际已扫描成功
            #         time.sleep(5)
            #
