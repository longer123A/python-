from python_ERP.Common.BasePage import BasePage
from python_ERP.PageLocators.list_of_caigou import ListChas as loc
import time
from python_ERP.Common import logger
import logging
class ListPu(BasePage):

    #输入SKU并且搜索
    def input_SUK(self,sku):
        logging.info('采购单：输入SKU_搜索')
        self.click_element(loc.list_chas,model='点击采购单列表')            #点击采购单列表
        # self.wait_eleVisible(loc.list_sku, model=name)
        self.input_text(loc.list_sku, sku,model='输入SKU')           #输入sku
        time.sleep(0.5)
        self.click_element(loc.seek_btn, model='点击搜索按钮')            #点击搜索



    #外部订单号
    def order_number(self):
        return self.get_text(loc.order_number,model='获取外部订单号，用于判断是否为空')     #获取外部订单号，用于判断是否为空（阿里账期和线上现结，需要添加外部订单号）

    #填写快递单号
    def input_expressage(self,numbers):
        name = '填写快递单号'
        logging.info('填写快递单号：{0}'.format(numbers))
        self.click_element(loc.express,model='点击快递单号')                  #点击快递号
        time.sleep(0.5)
        self.input_text(loc.input_express,numbers,model='输入快递单号')       #输入快递号（快递号为平台订单号）
        self.click_element(loc.express_conf,model='点击确认按钮')             #点击确认按钮
        time.sleep(4)

    #确认采购按钮
    def confirm_purchase(self):
        logging.info('确认采购下单')
        self.click_element(loc.confirm_order,model='点击确认采购按钮')            #点击确认采购按钮
        time.sleep(0.5)
        self.click_element(loc.confir_ok,model='点击确认按钮')                #点击OK按钮
        time.sleep(0.5)
        self.click_element(loc.confir_ok, model='二次确认')               #二次确认


    def get_xuhao(self):
        return self.get_text(loc.order_xuhao, model='获取订单号，用于断言订单是pass是否正常')           #获取订单号，用于断言订单是pass是否正常
    #批量操作
    # 快递单号：number
    def bulk_operation(self,sku,number):
        logging.info('确认是否可付款 或 是否需确认')
        time.sleep(3)
        self.click_element(loc.list_chas,model='点击采购单列表')   #点击采购单列表
        time.sleep(3)
        self.input_text(loc.list_sku,sku,model='输入SKU查询')      #输入sku查询采购按
        time.sleep(0.5)
        self.click_element(loc.seek_btn,model='sku查询按钮')       #点击搜索按钮
        time.sleep(3)
        if self.get_money_way(loc.way_Money)==True:                #判断是否为阿里账期或线上现结
            if self.order_number() =='':                           #判断外部订单号是否为空
                logging.info('外部订单号为空')
                time.sleep(3)
                self.click_element(loc.choose_btn, model='勾选订单')     #勾选订单
                self.click_element(loc.bulk_option, model='选择批量操作')    #选择批量操作
                time.sleep(0.5)
                if self.isElementExist(loc.modify_order,model='判断修改采购单是否存在')==True:
                    self.click_element(loc.modify_order,model='选择修改采购单')    #选择修改采购单
                    time.sleep(0.5)
                    self.switchover_html(1,model='切换html页面')
                    self.input_text(loc.input_order_number,number,model='输入采购单')   #输入采购单号（与快递单号一致）
                    self.driver.switch_to.default_content()
                    self.click_element(loc.confir_ok,model='点击确认按钮')       #确认按钮
                # ~~~~~~~~~~~~~~~~~~~~外部订单号填写成功~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                else:
                    self.click_element(loc.order_bji,model='点击编辑按钮')
                    time.sleep(1)
                    self.input_text(loc.bji_order_number,number,model='输入订单号')
                    time.sleep(0.5)
                    self.click_element(loc.bji_ok,model='确认修改')
                    self.get_alert()
                    time.sleep(1)
                logging.info('是否需要确认')
                time.sleep(4)
                self.click_element(loc.choose_btn, model='勾选订单')     #勾选订单
                self.click_element(loc.bulk_option, model='选择批量操作')    #选择批量操作
                self.click_element(loc.bulk_affirm, model='点击确认按钮')    #确认
                time.sleep(1)
                self.click_element(loc.confir_ok, model='点击确认按钮')      #OK
                time.sleep(5)
                #~~~~~~~~~~~~~~~~~~~~~~~填写物流单号~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                self.input_expressage(number)                       #填写物流单号
                self.confirm_purchase()                             #确认采购操作
            else:
                logging.info('订单号不为空')
                self.click_element(loc.choose_btn, model='勾选订单')
                self.click_element(loc.bulk_option, model='选择批量操作')
                self.click_element(loc.bulk_affirm,model='点击确认按钮')
                time.sleep(1)
                self.click_element(loc.confir_ok,model='点击确认按钮')
                time.sleep(5)
                self.input_expressage(number)
                self.confirm_purchase()
        else:
            logging.info('其他结款方式')
            time.sleep(1)
            self.click_element(loc.choose_btn, model='勾选订单')
            time.sleep(1)
            self.click_element(loc.bulk_option, model='选择批量操作')
            time.sleep(1)
            self.click_element(loc.bulk_affirm, model='点击确认按钮')
            time.sleep(1)
            self.click_element(loc.confir_ok, model='点击确认按钮')
            time.sleep(3)
            time.sleep(1)
            self.click_element(loc.choose_btn, model='勾选订单')
            time.sleep(1)
            self.click_element(loc.bulk_option, model='选择批量操作')
            time.sleep(1)
            self.click_element(loc.bulk_Money, model='点击确认按钮')
            time.sleep(1)
            self.click_element(loc.confir_ok, model='点击确认按钮')
            time.sleep(5)
            self.input_expressage(number)
            self.confirm_purchase()

