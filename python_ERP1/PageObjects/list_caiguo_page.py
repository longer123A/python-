from python_ERP1.Common.BasePage import BasePage
from python_ERP1.PageLocators.list_of_caigou import ListChas as loc
import time
from python_ERP1.Common import logger
import logging
class ListPu(BasePage):

    #输入SKU并且搜索
    def input_SUK(self,sku):
        name = "输入SKU_搜索"
        self.click_element(loc.list_chas,model=name)
        self.wait_eleVisible(loc.list_sku, model=name)
        self.input_text(loc.list_sku, sku,model=name)
        time.sleep(0.5)
        self.click_element(loc.seek_btn, model=name)


    #线上现结  阿里账期
    # def purcha_order(self):
    #     nama = '判断结款方式'
    #     self.wait_eleVisible(loc.way_Money,model=nama)
    #     ssfs = self.driver.find_element_by_xpath('//table[@id="data-list"]//tbody//tr[1]//td[8]').text
    #     return ssfs

    #外部订单号
    def order_number(self):
        nama = '获取外部订单号'
        self.wait_eleVisible(loc.order_number,model=nama)
        return self.get_text(loc.order_number,model=nama)

    #填写快递单号
    def input_expressage(self,numbers):
        name = '填写快递单号'
        logging.info('快递单号：{0}'.format(numbers))
        self.wait_eleVisible(loc.express,model=name)
        self.click_element(loc.express,model=name)
        time.sleep(0.5)
        self.input_text(loc.input_express,numbers,model=name)
        self.click_element(loc.express_conf,model=name)
        time.sleep(4)

    #确认采购按钮
    def confirm_purchase(self):
        nama = '确认采购下单'
        self.wait_eleVisible(loc.confirm_order,model=nama)
        self.click_element(loc.confirm_order,model=nama)
        time.sleep(0.5)
        self.click_element(loc.confir_ok,model=nama)
        time.sleep(0.5)
        self.click_element(loc.confir_ok, model=nama)

    #批量操作
    # 快递单号：number
    def bulk_operation(self,sku,number):
        nama = '确认是否可付款 或 是否需确认'
        time.sleep(3)
        self.click_element(loc.list_chas,model='点击采购单列表')
        time.sleep(3)
        self.wait_eleVisible(loc.list_sku,model='输入SKU')
        self.input_text(loc.list_sku,sku,model='输入SKU查询')
        time.sleep(0.5)
        self.click_element(loc.seek_btn,model='sku查询按钮')
        time.sleep(3)
        if self.get_money_way(loc.way_Money)==True:
            if self.order_number() =='':
                nama = '外部订单号为空'
                time.sleep(3)
                self.wait_eleVisible(loc.bulk_option, model=nama)
                #勾选第一个
                self.click_element(loc.choose_btn, model=nama)
                #选择批量操作
                self.click_element(loc.bulk_option, model=nama)
                #选择修改采购单
                time.sleep(0.5)
                self.click_element(loc.modify_order,model=nama)
                time.sleep(0.5)
                self.switchover_html(1,model=nama)
                #输入外部订单号
                self.input_text(loc.input_order_number,number,model=nama)
                self.driver.switch_to.default_content()
                #确认
                self.click_element(loc.confir_ok,model=nama)
                # buyerId
                # ~~~~~~~~~~~~~~~~~~~~外部订单号填写成功~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                nama = '是否需要确认'
                time.sleep(4)
                self.wait_eleVisible(loc.bulk_option, model=nama)
                # 勾选第一个
                self.click_element(loc.choose_btn, model=nama)
                # 选择批量操作
                self.click_element(loc.bulk_option, model=nama)
                # 选择确认
                self.click_element(loc.bulk_affirm, model=nama)
                # 选择OK
                time.sleep(1)
                self.click_element(loc.confir_ok, model=nama)
                time.sleep(5)
                #~~~~~~~~~~~~~~~~~~~~~~~填写物流单号~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                self.input_expressage(number)
                self.confirm_purchase()
            else:
                nama = '订单号不为空'
                logging.info('{0}'.format(nama))
                self.wait_eleVisible(loc.bulk_option, model=nama)
                # 勾选第一个
                self.click_element(loc.choose_btn, model=nama)
                # 选择批量操作
                self.click_element(loc.bulk_option, model=nama)
                #选择确认
                self.click_element(loc.bulk_affirm,model=nama)
                #选择OK
                time.sleep(1)
                self.click_element(loc.confir_ok,model=nama)
                time.sleep(5)
                self.input_expressage(number)
                self.confirm_purchase()
        else:
            logging.info('其他结款方式')
            self.wait_eleVisible(loc.choose_btn, model=nama)
            time.sleep(1)
            # 勾选第一个
            self.click_element(loc.choose_btn, model=nama)
            # 选择批量操作
            time.sleep(1)
            self.click_element(loc.bulk_option, model=nama)
            # 选择确认
            time.sleep(1)
            self.click_element(loc.bulk_affirm, model=nama)
            # 选择OK
            time.sleep(1)
            self.click_element(loc.confir_ok, model=nama)
            time.sleep(3)
            self.wait_eleVisible(loc.bulk_option, model=nama)
            # 勾选第一个
            time.sleep(1)
            self.click_element(loc.choose_btn, model=nama)
            # 选择批量操作
            time.sleep(1)
            self.click_element(loc.bulk_option, model=nama)
            # 选择确认
            time.sleep(1)
            self.click_element(loc.bulk_Money, model=nama)
            # 选择OK
            time.sleep(1)
            self.click_element(loc.confir_ok, model=nama)
            time.sleep(5)
            self.input_expressage(number)
            self.confirm_purchase()

