
from python_ERP1.Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
class KuCun(BasePage):

    def get_kucun(self,sku):
        self.wait_eleVisible((By.XPATH,'//*[@id="menu_11000000"]'))
        self.click_element((By.XPATH,'//*[@id="menu_11000000"]'))

        # 点击大浪仓库
        self.wait_eleVisible((By.XPATH,'//*[@id="menu_11110000_false_01"]/a'))
        self.click_element((By.XPATH, '//*[@id="menu_11110000_false_01"]/a'))

        #输入SKU
        self.wait_eleVisible((By.XPATH, '//*[@id="product-sku"]'))
        self.input_text((By.XPATH, '//*[@id="product-sku"]'),sku)

        #点击搜索
        self.wait_eleVisible((By.XPATH, '//*[@id="search-form"]/div/div[2]/button[1]'))
        self.click_element((By.XPATH, '//*[@id="search-form"]/div/div[2]/button[1]'))

        time.sleep(3)
        #
        return int(self.get_text((By.XPATH, '//table[@id="data-list"]/tbody//tr[1]//td[8]')))