from python_ERP.Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import logging
from python_ERP.Common import logger
class YunPipei(BasePage):

    #系统配置
    system = (By.XPATH,'//*[@id="menu_10000000"]')
    #运输方式匹配
    yunshu = (By.XPATH,'//*[@id="menu_10000000"]//*[@id="menu_10121000"]')
    #运输条件代码
    yunshu_dai = (By.XPATH,'//*[@id="s2id_logistics-type"]')
    #运输条件代码输入
    yunshu_dai_input = (By.XPATH,'//*[@id="s2id_autogen2_search"]')
    #运输条件确认
    yunshu_ok = (By.XPATH,'//*[@id="select2-results-2"]')
    #搜索按钮
    seek_button = (By.XPATH,'//button[@class="btn btn-sm green"]')
    #获取运输方式类型
    get_yunshu_pip = (By.XPATH,'//*[@id="data-list"]/tbody//tr[1]//td[7]')
    #获取运输方式类型
    def get_yunshu(self,motd):
        logging.info("获取运输匹配方式")
        self.click_element(self.system,model='点击系统配置')
        time.sleep(1)
        self.click_element(self.yunshu,model='点击运费方式匹配')
        time.sleep(2)
        self.click_element(self.yunshu_dai,model='点击筛选运输添加代码')
        time.sleep(1)
        self.input_text(self.yunshu_dai_input,motd,model='运输条件代码输入')
        self.click_element(self.yunshu_ok,model='运输条件确认')
        time.sleep(0.5)
        self.click_element(self.seek_button,model='点击搜索按钮')
        time.sleep(2)
        return str(self.get_text(self.get_yunshu_pip,model='返回运输方式类型'))