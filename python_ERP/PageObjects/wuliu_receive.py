from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from python_ERP.Common.BasePage import BasePage
import time
import re
from python_ERP.PageObjects.my_sql import MySql
import logging
from python_ERP.Common import logger
class Wuliu(BasePage):

    #订单管理
    order_guanli = (By.XPATH,'//*[@id="menu_13000000"]')

    #物流收包
    wuliu_receive = (By.XPATH,'//*[@id="menu_13101700"]/a')

    #输入跟踪号
    input_code = (By.XPATH,'//*[@id="orderTranNoId"]')

    #打印按钮
    print_button = (By.XPATH,'//*[@onclick="printPackage()"]')

    #包裹称重扫描
    baog_cheng = (By.XPATH,'//*[@id="menu_13110000"]//*[@id="menu_13113900"]')

    #序列号扫描
    xulihao_scan = (By.XPATH,'//*[@id="serialnumber"]')

    #包裹扫描
    baog_scan = (By.XPATH,'//*[@id="menu_13110000"]//*[@id="menu_13111800"]')

    #包裹称重扫描OK
    baog_cheng_ok = (By.XPATH,'//*[@data-id="ok"]')

    #包裹扫描
    baog_scan_click = (By.XPATH,'//*[@id="s2id_logistics-type"]/a')
    baog_scan_input = (By.XPATH, '//*[@id="s2id_autogen1_search"]')
    baog_scan_click_wuliu = (By.XPATH, '//*[@id="select2-results-1"]')

    def wuliu_scna(self,dingdan_code):
        logging.info("物流收包操作")
        self.click_element(self.order_guanli,model='点击订单管理')
        self.click_element(self.wuliu_receive,model='点击物流收包')
        time.sleep(3)
        self.input_text(self.input_code,dingdan_code,model='输入输入跟踪号')
        time.sleep(1)
        self.click_element(self.print_button,model='点击打印按钮')
        time.sleep(2)
        self.window_switch(-1)
        time.sleep(0.5)
        get_xulihao = self.get_text((By.XPATH,'//*[@id="printContent"]//div[4]/div//div'),model='获取序列号')
        xulihao=re.findall(r"\d+\.?\d*",get_xulihao)
        time.sleep(0.5)
        self.window_switch(-2)
        time.sleep(2)


        logging.info('包裹称重扫描')
        self.click_element(self.order_guanli, model='点击订单管理')
        self.click_element(self.baog_cheng, model='点击包裹称重扫描')
        time.sleep(2)
        self.input_text(self.xulihao_scan,xulihao,model='输入序列号')
        self.get_element(self.xulihao_scan).send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_element(self.baog_cheng_ok,model='确认')
        time.sleep(1)

        # nama = '包裹扫描'
        # self.click_element(self.order_guanli, model=nama)
        # self.click_element(self.baog_scan, model=nama)
        # time.sleep(2)
        # self.click_element(self.baog_scan_click,model=nama)
        # time.sleep(0.5)
        #
        # self.input_text(self.baog_scan_input,"夏浦物流",model=nama)
        # time.sleep(0.5)
        # self.click_element(self.baog_scan_click_wuliu,model=nama)
        # time.sleep(1)
        # self.input_text(self.xulihao_scan,xulihao, model=nama)
        # self.get_element(self.xulihao_scan).send_keys(Keys.ENTER)
        # time.sleep(1)

    baog_scan_click_qx=(By.XPATH,'//*[@class="nav nav-tabs custom"]//*[@id="menu_13111800"]/a')
    baog_scan_click_wuliu1 = (By.XPATH,'//*[@id="select2-results-1"]//li[1]')
    baog_scan_click_wuliu2 = (By.XPATH,'//*[@id="select2-results-1"]//li[2]')
    baog_scan_click_wuliu3 = (By.XPATH,'//*[@id="select2-results-1"]//li[3]')
    def wuliu_scna_qx(self,dingdan_code,mold):
        ss=MySql().get_scan(mold)

        logging.info("物流收包操作")
        self.click_element(self.order_guanli,model='点击订单管理')
        self.click_element(self.wuliu_receive,model='点击物流收包')
        time.sleep(3)
        self.input_text(self.input_code,dingdan_code,model='输入输入跟踪号')
        time.sleep(1)
        self.click_element(self.print_button,model='点击打印按钮')
        time.sleep(2)
        self.window_switch(-1)
        time.sleep(0.5)
        get_xulihao = self.get_text((By.XPATH,'//*[@id="printContent"]//div[4]/div//div'),model='获取序列号')
        xulihao=re.findall(r"\d+\.?\d*",get_xulihao)
        time.sleep(0.5)
        self.window_switch(-2)
        time.sleep(2)


        nama = '包裹称重扫描'
        self.click_element(self.order_guanli, model=nama)
        self.click_element(self.baog_cheng, model=nama)
        time.sleep(2)
        self.input_text(self.xulihao_scan,xulihao,model=nama)
        self.get_element(self.xulihao_scan).send_keys(Keys.ENTER)
        time.sleep(1)
        # self.click_element(self.baog_cheng_ok,model=nama)
        time.sleep(3)

        nama = '包裹扫描'
        self.click_element(self.order_guanli, model=nama)
        time.sleep(0.7)
        self.click_element(self.baog_scan, model=nama)
        time.sleep(2)
        self.click_element(self.baog_scan_click,model=nama)
        time.sleep(1)
        s_mold = str(mold)
        logging.info('s_mold:{0}'.format(s_mold))
        tt = s_mold.split("(")
        logging.info('tt:{0}'.format(tt))
        get_moth_index1 = tt[-1]
        logging.info('get_moth_index1:{0}'.format(get_moth_index1))
        try:
            yy = ss[0][0]
            logging.info('获取yy:{0}'.format(yy))
            get_moth_index = yy.split("-")
            logging.info('获取get_moth_index:{0}'.format(get_moth_index))

            self.input_text(self.baog_scan_input,get_moth_index[0],model=nama)
        except:
            self.input_text(self.baog_scan_input, get_moth_index1[0:-1], model=nama)
        finally:
            time.sleep(0.5)
            self.click_element(self.baog_scan_click_wuliu1,model=nama)
            time.sleep(1)
            self.input_text(self.xulihao_scan,xulihao, model=nama)
            self.get_element(self.xulihao_scan).send_keys(Keys.ENTER)
            get_text=(By.XPATH,'//*[@id="scan_datas"]/div')
            if "与选择物流不匹配" in self.get_text(get_text,model="判断物流是否匹配"):
                self.click_element(self.baog_scan_click, model=nama)
                self.input_text(self.baog_scan_input, get_moth_index1[0:-1], model=nama)
                time.sleep(0.5)
                self.click_element(self.baog_scan_click_wuliu2, model=nama)
                time.sleep(1)
                self.input_text(self.xulihao_scan, xulihao, model=nama)
                self.get_element(self.xulihao_scan).send_keys(Keys.ENTER)
                if "与选择物流不匹配" in self.get_text(get_text, model="判断物流是否匹配"):
                    self.click_element(self.baog_scan_click, model=nama)
                    self.input_text(self.baog_scan_input, get_moth_index1[0:-1], model=nama)
                    time.sleep(0.5)
                    self.click_element(self.baog_scan_click_wuliu3, model=nama)
                    time.sleep(1)
                    self.input_text(self.xulihao_scan, xulihao, model=nama)
                    self.get_element(self.xulihao_scan).send_keys(Keys.ENTER)

            time.sleep(1)
# """
    #状态
    status = (By.XPATH,'//*[@id="out-status"]')
    status2 = (By.XPATH,'//*[@id="out-status"]//option[1]')

    #订单号
    dingdan_code = (By.XPATH,'//*[@id="search-value"]')

    #获取内容
    get_text1 = (By.XPATH,'//*[@id="package-list"]/tbody/tr[1]/td[14]')

    #搜索按钮
    seek_button = (By.XPATH,'//*[@id="search-form"]//button[1]')
    #断言用
    def judge_order_cku(self,dingdan_code):
        logging.info("获取订单状态断言")
        self.click_element(self.order_guanli,model='点击订单管理')
        self.click_element(self.wuliu_receive,model='点击物流收包')
        time.sleep(4)
        self.input_text(self.dingdan_code,dingdan_code,model='输入输入跟踪号')
        time.sleep(1)
        self.click_element(self.status,model='筛选状态选择')
        time.sleep(1)
        self.click_element(self.status2,model='选择所有')
        time.sleep(1)
        self.click_element(self.seek_button,model='点击搜索按钮')
        time.sleep(2)
        return str(self.get_text(self.get_text1,model='返回订单状态'))