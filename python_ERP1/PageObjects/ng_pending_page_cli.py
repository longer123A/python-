from python_ERP1.Common.BasePage import BasePage
from python_ERP1.PageLocators.ng_pending_caigoucl import NgPending as loc
import time
from python_ERP1.Common import logger
import logging
from selenium.webdriver.common.keys import Keys
class NgPending(BasePage):

    #获取NG采购待处理订单
    def get_pending(self,sku,mode):
        name = '获取NG采购待处理订单'
        self.wait_eleVisible(loc.receive_dispatch,model=name)
        self.click_element(loc.receive_dispatch,model=name)
        self.click_element(loc.ng_pending,model=name)
        time.sleep(2)
        self.wait_eleVisible(loc.sku_input,model=name)
        self.input_text(loc.sku_input,sku,model=name)
        time.sleep(0.5)
        self.click_element(loc.seek_button,model=name)
        time.sleep(3)
        self.dispose(mode)

    #处理订单
    def dispose(self,mode):
        nama = '订单开始处理'
        self.wait_eleVisible(loc.noe_dan,model=nama)
        self.click_element(loc.noe_dan,model=nama)

        time.sleep(0.5)
        self.click_element(loc.ng_procu,model=nama)
        time.sleep(1)
        if  mode=='pass':
            self.click_element(loc.pass_che,model=nama)
            time.sleep(1)
            self.input_text(loc.pass_text,'pass',model='输入pass理由')
            time.sleep(1)
            self.click_element(loc.button_ok,model='OK')
            time.sleep(3)
        else:
            self.click_element(loc.ng_che,model=nama)
            time.sleep(1)
            self.input_text(loc.ng_text,'NG',model='输入NG理由')
            time.sleep(0.5)
            self.click_element(loc.result,model=nama)
            self.input_text(loc.result_input,'NG结果输入',model='结果输入操作')
            time.sleep(0.5)
            self.get_element(loc.result_input).send_keys(Keys.ENTER)
            time.sleep(0.5)
            self.click_element(loc.button_ok, model='OK')
            time.sleep(3)