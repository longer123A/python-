from selenium.webdriver.common.keys import Keys
from python_ERP1.Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from python_ERP1.PageObjects.my_sql import MySql
from python_ERP1.PageObjects.ng_pending_page_cli import NgPending
#入库扫描方法

class Scan(BasePage):

    #收发货管理
    delivery = (By.XPATH,'//*[@id="menu_13000000"]/a')
    #回货扫描
    back_scan = (By.XPATH,'//*[@id="menu_13131400"]/a')
    #快递单号
    ex_input = (By.XPATH,'//*[@id="expressId"]')

    def back_to_scan(self,number):
        nama = '回货扫描'
        self.wait_eleVisible(self.delivery,model=nama)
        self.click_element(self.delivery,model=nama)
        self.click_element(self.back_scan,model=nama)
        self.input_text(self.ex_input,number,model=nama)
        self.get_element(self.ex_input).send_keys(Keys.ENTER)
        time.sleep(1)




    #快递单号查询
    ex_scan=(By.XPATH,'//div[@class="col-md-12"]//li[2]')
    #快递单号输入
    ex_to_input = (By.XPATH,'//*[@id="expressId"]')
    #入库数量
    inven_quan = (By.XPATH,'//input[@name="inStock.items[0].quantity"]')
    #生成入库单
    gen_the_rec = (By.XPATH,'//button[@class="btn btn-default btn-xs"]')

    def ex_to_scan(self,number,size):
        nama = '快递单号扫描'
        self.wait_eleVisible(self.ex_scan, model=nama)
        self.click_element(self.ex_scan, model=nama)
        time.sleep(1)
        self.input_text(self.ex_to_input, number, model=nama)
        time.sleep(0.5)
        self.get_element(self.ex_to_input).send_keys(Keys.ENTER)
        time.sleep(2)
        self.input_text(self.inven_quan,size,model='入库数量')
        time.sleep(1)
        self.click_element(self.gen_the_rec,model='生成入库单')
        time.sleep(1)
        self.get_alert()
        time.sleep(3)


    #qc扫描
    qc_scan = (By.XPATH,'//div[@class="col-md-12"]//li[4]')
    #二维码输入扫描
    qr_input = (By.XPATH,'//*[@id="uuidAndSku"]')
    #二次确认
    qr_affirm = (By.XPATH,'//button[@data-id="ok"]')
    #采购数量
    order_size = (By.XPATH,'//table[@id="item-list"]//td[8]')
    #确认
    pass_ok = (By.XPATH,'//*[@id="pass-top-a"]')
    #尺寸输入
    table_loc =(By.XPATH,'//form[@id="qcRecordForm"]')
    table_loc_2='//form[@id="qcRecordForm"]'
    input_loc = (By.XPATH,'//*[@id="qcRecordLength"]')
    #是否为全检产品
    # comp_tion = (By.XPATH,'//*[@id="instock-cell"]/h3/span[4]/span[2]')
    # comp_tion_2='//*[@id="instock-cell"]/h3/span[4]/span[2]'
    #获取抽检个数//*[@id="checkQuantity"]
    quantity = (By.XPATH,'//*[@id="checkQuantity"]')

    def qc_to_scan(self,sku):
        time.sleep(1)
        name = 'QC扫描'

        self.wait_eleVisible(self.qc_scan,model=name)
        self.click_element(self.qc_scan,model=name)
        time.sleep(2)
        input_qr_code = str(MySql().get_sku(sku, 1)[0][0]) + '.' + sku
        self.wait_eleVisible(self.qr_input,model='二维码输入检查')
        #二维码
        self.input_text(self.qr_input,input_qr_code,model='二维码输入')
        time.sleep(1)
        self.get_element(self.qr_input).send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_element(self.qr_affirm, model='二次确认')
        time.sleep(1)
        get_quantity =self.get_text(self.quantity,model='获取抽检数量')
        if int(get_quantity)==1:
            time.sleep(1)
            if  self.isElementExist_2(self.table_loc_2)==True:
                self.wait_eleVisible(self.table_loc, model='需要输入尺寸')
                self.input_text(self.input_loc, 1, model='输入尺寸')
                time.sleep(0.5)
                # ~~~~~~~~~~~~~~~~~~后面需要判断采购数量是否正确~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                self.click_element(self.pass_ok, model='确认通过')
                time.sleep(1)
                self.click_element(self.qr_affirm, model='服装类良品')
                time.sleep(1)
                self.rku_to_scan(input_qr_code)
            else:
                self.click_element(self.pass_ok, model='确认通过')
                time.sleep(1)
                self.click_element(self.qr_affirm, model='良品')
                self.rku_to_scan(input_qr_code)
        else:
            get_qr=MySql().get_sku(sku,int(get_quantity))
            for i in range(len(get_qr)):
                for get_qr_code in get_qr[i][0]:
                    qr=get_qr_code+'.'+sku
                    self.input_text(self.qr_input, qr, model='二维码输入')
                    time.sleep(1)
                    self.get_element(self.qr_input).send_keys(Keys.ENTER)
                    time.sleep(1)
                    self.click_element(self.qr_affirm, model='二次确认')
                    time.sleep(1)

            else:
                if  self.isElementExist_2(self.table_loc_2) == True:
                    self.wait_eleVisible(self.table_loc, model='需要输入尺寸')
                    self.input_text(self.input_loc, 1, model='输入尺寸')
                    time.sleep(0.5)
                    # ~~~~~~~~~~~~~~~~~~后面需要判断采购数量是否正确~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    self.click_element(self.pass_ok, model='确认通过')
                    time.sleep(1)
                    self.click_element(self.qr_affirm, model='服装类良品')
                    time.sleep(1)
                    self.rku_to_scan(input_qr_code)
                else:
                    self.click_element(self.pass_ok, model='确认通过')
                    time.sleep(1)
                    self.click_element(self.qr_affirm, model='良品')
                    self.rku_to_scan(input_qr_code)

    #入库扫描
    rku_scan = (By.XPATH,'//*[@class="col-md-12"]//li[5]')
    #二维码扫描
    qr_rk_scan = (By.XPATH,'//*[@id="uuidAndSku"]')
    def rku_to_scan(self,qr):
        time.sleep(1)
        name = '入库扫描'
        self.wait_eleVisible(self.rku_scan,model=name)
        self.click_element(self.rku_scan,model=name)
        time.sleep(1)
        self.input_text(self.qr_rk_scan,qr,model=name)
        time.sleep(0.5)
        self.get_element(self.qr_rk_scan).send_keys(Keys.ENTER)
        time.sleep(2)


    #NG不通过按钮
    ng_no = (By.XPATH,'//*[@id="ng-top"]')
    #不良原因输入框
    bad_input = (By.XPATH,'//*[@id="s2id_autogen1_search"]')
    #尺寸不符
    size_no = (By.XPATH,'//*[@id="select2-drop"]//li[2]')
    #颜色不符
    tinct_on = (By.XPATH,'//*[@id="select2-drop"]//li[3]')
    #款式不符
    style_on = (By.XPATH,'//*[@id="select2-drop"]//li[4]')
    #二次确认
    ng_ok = (By.XPATH,'//*[@data-id="ok"]')
    #下一步
    next_input = (By.XPATH,'//*[@class="ui-dialog-grid"]//*[@id="target-status"]')

    #NG状态
    #reason：不良品原因
    #statu:下一步
    def qc_ng_scan(self,sku,reason='',statu=''):
        time.sleep(1)
        name = 'QC扫描'
        self.wait_eleVisible(self.qc_scan,model=name)
        self.click_element(self.qc_scan,model=name)
        time.sleep(2)
        input_qr_code = str(MySql().get_sku(sku, 1)[0][0]) + '.' + sku
        self.wait_eleVisible(self.qr_input,model='二维码输入检查')
        #二维码
        self.input_text(self.qr_input,input_qr_code,model='二维码输入')
        time.sleep(1)
        self.get_element(self.qr_input).send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_element(self.qr_affirm, model='二次确认')
        time.sleep(1)
        #~~~~~~~~~~~~~~~~~~~~~~~~修改NG内容~~~~~~~~~~~~~~~~~~~~~
        self.wait_eleVisible(self.ng_no,model='NG按钮检查')
        self.click_element(self.ng_no,model='NG按钮点击')
        time.sleep(1)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~理由分割线~~~~~~~~~~~~~~~~~~~~
        if reason=='':
            self.input_text(self.bad_input, '不良理由记录', model='输入不良理由')
            self.get_element(self.bad_input).send_keys(Keys.ENTER)
            time.sleep(1)
            if statu=='':
                self.click_element(self.ng_ok,model='确认')
                time.sleep(2)
            else:
                self.select(self.next_input,'NG入库待处理',model='选择NG入库待处理')
                time.sleep(2)

        elif reason=='尺寸':
            self.click_element(self.size_no,model='尺寸不符')
            time.sleep(2)
            if statu=='':
                self.click_element(self.ng_ok,model='确认')
                time.sleep(2)
            else:
                self.select(self.next_input,'NG入库待处理',model='选择NG入库待处理')
                time.sleep(2)

        elif reason=='颜色':
            self.click_element(self.tinct_on, model='颜色不符')
            time.sleep(1)
            if statu=='':
                self.click_element(self.ng_ok,model='确认')
                time.sleep(2)
            else:
                self.select(self.next_input,'NG入库待处理',model='选择NG入库待处理')
                time.sleep(2)
        elif reason=='款式':

            self.click_element(self.style_on, model='款式不符')
            time.sleep(2)
            if statu=='':
                self.click_element(self.ng_ok,model='确认')
                time.sleep(2)
            else:
                self.select(self.next_input,'NG入库待处理',model='选择NG入库待处理')
                time.sleep(2)
        else:
            print('参数错误')