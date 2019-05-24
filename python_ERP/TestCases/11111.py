# from selenium import webdriver
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from python_ERP.Common.dir_config import *
# from selenium.webdriver.support.ui import Select
# # textdata_dir
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://192.168.99.203:8080/pss/login')
# WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login-btn"]')))
# #登录
# driver.find_element_by_xpath('//*[@id="username"]').send_keys('it_test')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('111')
# driver.find_element_by_xpath('//*[@id="captcha"]').send_keys('111')
# driver.find_element_by_xpath('//*[@id="login-btn"]').click()
# #
# time.sleep(2)
# driver.get('http://192.168.99.203:8080/pss/products')
# time.sleep(2)
#
# driver.switch_to.frame("content")
# driver.find_element_by_xpath('//*[@id="product-sku"]').send_keys('0A593C')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="search-form"]/div/div[2]/button[1]').click()
# # driver.switch_to.default_content()
# time.sleep(2)
#
# driver.find_element_by_xpath('//*[@name="checkAll"]').click()
# time.sleep(0.5)
# #
# ele = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/form[1]/div[1]/select')
#
# s = Select(ele)
# s.select_by_visible_text('批量修改采购、上下架')
# time.sleep(1)
# #
# driver.switch_to.frame(0)
# ele = driver.find_element_by_xpath('//*[@name="product.listingStatus"]')
#
# s = Select(ele)
# s.select_by_visible_text('上架')
# time.sleep(1)
#
#
# ele = driver.find_element_by_xpath('//*[@name="product.isPurchase"]')
#
# s = Select(ele)
# s.select_by_visible_text('否')
# time.sleep(1)
#
#
# ele = driver.find_element_by_xpath('//*[@name="product.qcType"]')
#
# s = Select(ele)
# s.select_by_visible_text('1%比例抽样')
# time.sleep(1)
#
#
# ele = driver.find_element_by_xpath('//*[@name="product.packagingId"]')
#
# s = Select(ele)
# s.select_by_visible_text('带包装')
# time.sleep(1)
# # driver.switch_to.default_content()
# driver.switch_to.default_content()
# # from selenium.webdriver.common.action_chains import ActionChains
# driver.find_element_by_xpath('/html/body/div[3]/div/table')
# driver.find_element_by_xpath('//*[@data-id="ok"]').click()
# ele_2 = driver.find_element_by_xpath('//*[@data-id="ok"]')
#
# ActionChains(driver).click(ele_2).perform()

# for i in range(1,2):
# #         js='var q=document.documentElement.scrollTop=10'
# #         driver.execute_script(js)
# #         dict_xx = {}
# #         t=driver.find_element_by_xpath('//*[@id="data-table"]//tbody//tr[1]//td[1]/a').text
# #         tt=driver.find_element_by_xpath('//*[@id="data-table"]//tbody//tr[1]//td[2]/a').text
# #         # dict_xxx.append(t)
# #         # dict_xxx.append(":")
# #         # dict_xxx.append(tt)
# #         dict_xx[t]=dict_xx[tt]
# #         dict_xxx.append(dict_xx)
# # # //*[@id="data-table"]//tbody//tr["行"]//td["列"]/a     共159
# # #
# #
# #
# print(dict_xxx)
#
# s={"450自营仓DHL转运（内电）":"1"}
# print(s["450自营仓DHL转运（内电）"])

# def aaa():
#     a=111
#     if 1==1:
#         b=a
#         print(b)
# if __name__ == '__main__':
#     aaa()
    # elif BasePage(driver).get_text(xinxi2)==data:
    #     print(data)
    # elif BasePage(driver).get_text(xinxi3)==data:
    #     print(data)
    # elif BasePage(driver).get_text(xinxi4)==data:
    #     print(data)
    # elif BasePage(driver).get_text(xinxi5)==data:
    #     print(data)
# ssss=str(driver.find_element_by_id('select2-results-1').text)
# s=ssss.split('\n')
# for t in ssss:
#     if s in t:
#         pass
# print(ssss)
# print(s)
# driver.find_element_by_xpath('//*[@id="orderid"]').send_keys('PL20190511105051718')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="sku"]').send_keys('0A361B')
# driver.find_element_by_xpath('//*[@id="sku"]').send_keys(Keys.ENTER)
# time.sleep(1)
# sku2= driver.find_element_by_xpath("//*[@id='order-grid-1']//tbody").text
# sku3 = sku2.split(' ')
# driver.find_element_by_xpath('//*[@id="sku"]').send_keys(sku3[0])
# driver.find_element_by_xpath('//*[@id="sku"]').send_keys(Keys.ENTER)
#
# s=str(driver.find_element_by_xpath('//*[@id="scan-record"]').text)
# ss=s.split('\n')
# sss=s.split(' ')
# print('s{0}'.format(s))
# print("ss{0}".format(ss))
# print("sss{0}".format(sss))
#PL20190511103614577
# s=driver.find_element_by_xpath('//*[@id="order-list"]//tr[2]//td[5]').text
# print(s)

# self.get_element(self.input_sku).send_keys(Keys.ENTER)
# get_qr = self.get_text(self.get_qr, model=nama)
# logging.info('get_qr:{0}'.format(get_qr))
# qr = get_qr.split(' ')
# logging.info('qr1:{0}'.format(qr))
# logging.info('qr2:{0}'.format(qr[0][0:-19]))
# time.sleep(1)
# return qr[0][0:-19]  # 返回二维码序列号
#
# print(driver.find_element_by_xpath('//*[@id="printContent"]//div[4]/div//div').text)
#

# s = 1
# # xinxi = (By.XPATH, '//*[@id="data-list"]/tbody/tr[%s]/td[1]'.format(s))
# tt = 1
# xxx=""
# while tt == 1:
#    if xxx=="":
#       tt+=3
#       s += 1
#       xxx=1
# print(tt)
# s=1,2,3,4
# print(s[1:])


#
# s={'a':1}
# print(list(s.values())[0])
# #
# mold1='云途物流-德国邮政平邮（特惠12国）(043)'
# mold2="云途物流-法国专线(511)"
# mold3="速卖通线上发货-4PX新邮挂号小包(深圳仓)(033)"
#
# tt = mold3.split("(")
# get_moth_index1 =tt[-1]
# print(get_moth_index1[0:-1])
# ssss=['国）', '043']
# print(ssss[1])
# from python_ERP.TestDatas.baog_Data im
# port *
# def get_scan_wuliumold(get_moth_index):
#     # dict_data
#     # for get_wuliumoth in dict_data.values():
#         print(dict_data.values())
#         r=list(dict_data.values())
#         print(r.index("自营海外仓-DHL小包(美西仓)(转运)（内电）(D450)"))
#     # for rr in r:
    #     print(rr)
    #     if r.index("自营海外仓-DHL小包(美西仓)(转运)（内电）(D450)"):
    #         yyy=list(dict_data.values()).index(get_moth_index)
    #         return yyy
    #     else:
#     #         pass
# if __name__ == '__main__':
#     s=get_scan_wuliumold("")
s=int(input())
if s==2:
    print(s)