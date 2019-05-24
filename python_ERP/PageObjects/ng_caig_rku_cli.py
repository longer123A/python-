from python_ERP.Common.BasePage import BasePage
from python_ERP.PageLocators.ng_pending_caigoucl import NgPending as loc
import time
from python_ERP.Common import logger
import logging
from selenium.webdriver.common.keys import Keys
class NgPending(BasePage):

   #~~~~~~~~~~~~~~~~~~~~~~~~采购待处理~~~~~~~~~~~~~~~~~~~~~~~~
    #获取NG采购待处理订单
    def get_pending(self,sku,mode):
        logging.info('获取NG采购待处理订单')
        self.click_element(loc.receive_dispatch,model='点击收发货管理')     #收发货管理按钮
        self.click_element(loc.ng_pending,model='NG采购待处理按钮')           #NG采购待处理按钮
        time.sleep(2)
        self.input_text(loc.sku_input,sku,model='输入sku')           #输入sku
        time.sleep(0.5)
        self.click_element(loc.seek_button,model='点击搜索按钮')
        time.sleep(3)
        self.dispose(mode)                                      #订单处理

    #处理订单
    def dispose(self,mode):
        logging.info('订单开始处理')
        self.click_element(loc.noe_dan,model='勾选第一个订单')          #第一个订单勾选
        time.sleep(0.5)
        self.click_element(loc.ng_procu,model='NG采购操作栏')         #NG采购操作栏
        time.sleep(1)
        if  mode=='pass':                                   #pass订单
            self.click_element(loc.pass_che,model='#PASS')
            time.sleep(1)
            self.input_text(loc.pass_text,'pass',model='输入pass理由')
            time.sleep(1)
            self.click_element(loc.button_ok,model='OK')
            time.sleep(5)
        else:
            self.click_element(loc.ng_che,model='NG')
            time.sleep(1)
            self.input_text(loc.ng_text,'NG',model='输入NG理由')
            time.sleep(0.5)
            self.click_element(loc.result,model='处理结果')
            self.input_text(loc.result_input,'NG结果输入',model='结果输入操作')
            time.sleep(0.5)
            self.get_element(loc.result_input).send_keys(Keys.ENTER)
            time.sleep(0.5)
            self.click_element(loc.button_ok, model='OK')
            time.sleep(5)


    # ~~~~~~~~~~~~~~~~~~~~~~~~入库待处理~~~~~~~~~~~~~~~~~~~~~~~~
    def get_rku_pending(self,sku,mode):
        logging.info('获取NG采购待处理订单')
        self.click_element(loc.receive_dispatch,model='点击收发货管理')
        self.click_element(loc.ng_rku_pending,model='NG入库待处理')
        time.sleep(2)
        self.input_text(loc.sku_input,sku,model='输入sku')
        time.sleep(0.5)
        self.click_element(loc.seek_button,model='点击搜索按钮')
        time.sleep(3)
        self.rku_dispose(mode)

    def rku_dispose(self,mode):
        logging.info('订单开始处理')
        self.click_element(loc.noe_dan,model='勾选第一个订单')
        time.sleep(0.5)
        self.click_element(loc.ng_procu,model='点击NG采购操作栏')
        time.sleep(1)
        if  mode=='废弃':
            self.click_element(loc.abandon_yq,model='废弃')
            time.sleep(1)
            self.get_alert(model='废弃弹窗确认')
            time.sleep(3)
            cur_handles = self.driver.window_handles
            logging.info('窗口总数：{0}'.format(cur_handles))
            if len(cur_handles)==2:
                self.window_switch(0)
            else:
                return False
        elif mode=='passqc':
            self.click_element(loc.pass_qc, model='pass给QC')
            time.sleep(1)
            self.get_alert(model='pass给QC弹窗确认')
            time.sleep(2)
        else:
            self.click_element(loc.rku_ng, model='NG采购处理')
            time.sleep(1)
            self.get_alert(model='NG采购处理弹窗确认')
            time.sleep(2)