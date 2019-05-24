from python_ERP1.PageLocators.suggest_jianyi import SuPusing as loc
from python_ERP1.Common.BasePage import BasePage
import time
class GetOrdervalue(BasePage):


    #获取建议采购最后一个的SKU
    def get_order_sku(self):
        name = "SKU"
        #等待元素可见
        self.wait_eleVisible(loc.SKU,model=name)
        # 获取订单的SKU;
        return self.get_text(loc.SKU,model=name)

    #商品筛选条件
    def filtrate_order(self,money):
        nama = '订单筛选'
        self.wait_eleVisible(loc.money_way,model=nama)
        self.select(loc.money_way,money,model=nama)
        self.select(loc.status,'上架',model=nama)
        self.select(loc.way_tu,'否',model=nama)
        time.sleep(1)
        self.click_element(loc.seek_button,model=nama)
        time.sleep(1)

    #获取采购的数量
    def get_order_size(self):
        name = '数量'
        # 等待元素可见
        self.wait_eleVisible(loc.SKU, model=name)
        #获取采购的数量
        return int(self.get_element_attribute(loc.order_size,"value",model=name))

    #sku输入
    def input_sku(self,sku):

        nama = '输入SKU搜索'
        #等待元素可见
        self.wait_eleVisible(loc.input_sku, model=nama)
        self.input_text(loc.input_sku, sku , model=nama)
        time.sleep(1)
        self.click_element(loc.seek_button,model=nama)

    #选择商品
    def choose_order(self):
        nama = '勾选订单'
        #等待元素可见
        self.wait_eleVisible(loc.sp_choose, model=nama)
        self.click_element(loc.sp_choose,model=nama)
        time.sleep(1)
        self.click_element(loc.gen_chase_order,model=nama)

