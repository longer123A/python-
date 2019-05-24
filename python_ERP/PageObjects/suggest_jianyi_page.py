from python_ERP.PageLocators.suggest_jianyi import SuPusing as loc
from python_ERP.Common.BasePage import BasePage
import time
import logging
from python_ERP.Common import logger
class GetOrdervalue(BasePage):


    #获取建议采购最后一个的SKU
    def get_order_sku(self):
        return self.get_text(loc.SKU,model="SKU")

    #商品筛选条件
    def filtrate_order(self,money):
        logging.info('采购订单筛选')
        self.select(loc.money_way,money,model='选择结款方式')
        self.select(loc.status,'上架',model='选择上架')
        self.select(loc.way_tu,'否',model='选择否')
        time.sleep(1)
        self.click_element(loc.seek_button,model='点击搜索')
        time.sleep(2)
    def filtrate_order_qx(self):
        logging.info('采购订单筛选')
        self.select(loc.status,'上架',model='选择上架')
        self.select(loc.way_tu,'否',model='选择否')
        time.sleep(1)
        self.click_element(loc.seek_button,model='点击搜索')
        time.sleep(2)

    #获取采购的数量
    def get_order_size(self):
        return int(self.get_element_attribute(loc.order_size,"value",model='获取采购数量'))

    #sku输入
    def input_sku(self,sku):
        logging.info('输入SKU搜索')
        self.input_text(loc.input_sku, sku , model='输入SKU')
        time.sleep(1)
        self.click_element(loc.seek_button,model='点击搜索按钮')

    #选择商品
    def choose_order(self):
        logging.info('勾选订单')
        self.click_element(loc.sp_choose,model='勾选第一个订单')
        time.sleep(1)
        self.click_element(loc.gen_chase_order,model='生成采购单')

    #不存在订单是获取内容
    def get_no_text(self):
        return self.get_text(loc.no_order,model='订单不存在')
