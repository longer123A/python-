from python_ERP.Common.BasePage import BasePage
from python_ERP.PageLocators.stock_kucun_home import StockControl as loc
from python_ERP.PageLocators.suggest_jianyi import SuPusing as Sloc
import time
class PutStor(BasePage):

    #点击库存管理按钮
    def click_stocon(self):
        self.click_element(loc.stoco, model="点击库存管理按钮")

    #点击建议采购按钮
    def click_suging(self):
        self.click_element(loc.suging, model="点击建议采购按钮")
        time.sleep(3)