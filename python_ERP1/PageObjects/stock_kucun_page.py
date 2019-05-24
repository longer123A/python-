from python_ERP1.Common.BasePage import BasePage
from python_ERP1.PageLocators.stock_kucun_home import StockControl as loc
from python_ERP1.PageLocators.suggest_jianyi import SuPusing as Sloc
import time
class PutStor(BasePage):

    #点击库存管理按钮
    def click_stocon(self):
        nama = "点击库存管理按钮"
        self.wait_eleVisible(loc.stoco, model=nama)
        self.click_element(loc.stoco, model=nama)

    #点击建议采购按钮
    def click_suging(self):
        nama = "点击建议采购按钮"
        self.wait_eleVisible(loc.suging, model=nama)
        self.click_element(loc.suging, model=nama)
        time.sleep(3)