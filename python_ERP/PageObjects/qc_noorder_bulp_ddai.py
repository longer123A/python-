from python_ERP.Common.BasePage import BasePage
from python_ERP.PageLocators.qc_npgoods_bulp_ddai import NoGoode as loc
import time
import logging
from python_ERP.Common import logger
class NoGoodPage(BasePage):

    #QC不良品
    def nogood_dispose(self,sku,xuhao):
        logging.info('不良品订单处理')
        self.click_element(loc.receive_dispatch, model='等待QC订单处理')
        self.click_element(loc.qc_nocoode, model='等待QC订单处理')
        time.sleep(3)
        self.input_text(loc.sku,sku,model='SKU输入')
        self.input_text(loc.input_xuhao, xuhao, model='订单号输入')
        self.click_element(loc.seek_button,model='点击搜索按钮')
        time.sleep(3)

    def get_order(self):
        return  self.get_text(loc.get_text,model='判断订单是否存在')

    # 等待QC
    def wait_dispose(self, sku, xuhao):
        self.click_element(loc.receive_dispatch, model='等待QC订单处理')
        self.click_element(loc.wait_qc, model='等待QC订单处理')

        time.sleep(3)
        self.input_text(loc.sku, sku, model='SKU输入')
        self.input_text(loc.input_xuhao, xuhao, model='订单号输入')
        self.click_element(loc.seek_button, model='点击搜索按钮')
        time.sleep(3)

    def wait_order(self):
        return self.get_text(loc.get_text, model='判断订单是否存在')

    #废弃
    def feiqi_dispose(self, sku, xuhao):
        logging.info('废弃订单处理')
        self.click_element(loc.feiqi_order, model='点击废弃订单处理')
        time.sleep(3)
        self.input_text(loc.sku, sku, model='SKU输入')
        self.input_text(loc.input_xuhao, xuhao, model='订单号输入')
        self.click_element(loc.seek_button, model='点击搜索按钮')
        time.sleep(3)

    def get_feiqi(self):
        nama = '判断订单是否存在'
        return self.get_text(loc.get_text, model=nama)


    #待采购处理
    def get_daiccaigou(self, sku, xuhao):
        logging.info('待采购处理订单处理')
        self.click_element(loc.dai_caigou, model='待采购处理订单处理')

        time.sleep(3)
        self.input_text(loc.sku, sku, model='SKU输入')
        self.input_text(loc.input_xuhao, xuhao, model='订单号输入')
        self.click_element(loc.seek_button, model='点击搜索按钮')
        time.sleep(3)

    def get_daicg(self):
        nama = '判断订单是否存在'
        return self.get_text(loc.dai_caigou_text, model=nama)