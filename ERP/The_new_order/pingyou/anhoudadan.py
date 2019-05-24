#按货打单

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from python_ERP.Common.BasePage import BasePage

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.99.203:8080/pss/login')
WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login-btn"]')))
#登录
driver.find_element_by_xpath('//*[@id="username"]').send_keys('it_test')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('111')
driver.find_element_by_xpath('//*[@id="captcha"]').send_keys('111')
driver.find_element_by_xpath('//*[@id="login-btn"]').click()

# time.sleep(2)
# driver.get('http://192.168.99.203:8080/pss/orders/link?query.status=3')
#
#
# s=BasePage(driver)
# order_code_shai = (By.NAME,'query.searchType')
# s.select(order_code_shai,'平台订单号')
# 点击首页待合并
WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="menu_11000000"]/a')))
driver.find_element_by_xpath('//*[@id="menu_11000000"]/a').click()

#
WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="menu_11131400"]/a')))
driver.find_element_by_xpath('//*[@id="menu_11131400"]/a').click()

#
time.sleep(3)
driver.find_element_by_xpath('//*[@id="product-sku"]').send_keys('LLY71211102BK')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="search-form"]/div/div/button[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//input[@name="checkedSkuList"]').click()
driver.find_element_by_xpath('//*[@id="purchase-form"]//button[1]').click()
time.sleep(1)
WebDriverWait(driver,5).until(EC.alert_is_present())
alert = self.driver.switch_to.alert
alert.accept()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="menu_11131000"]/a').click()
time.sleep(60)



# #点击新建订单
# cur_handles = driver.window_handles
# driver.switch_to.window(cur_handles[-1])
# WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="searchForm"]/div/div[1]/button')))
# driver.find_element_by_xpath('//*[@id="searchForm"]/div/div[1]/button').click()
#
#
#创建订单
cur_handles = driver.window_handles
driver.switch_to.window(cur_handles[-1])
WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="platform-id"]')))
#选择平台
ele = driver.find_element_by_xpath('//*[@id="platform-id"]')
s = Select(ele)
s.select_by_visible_text('AliExpress')
time.sleep(0.5)

#输入平订单号
import random
order=random.randint(100000,1000000)
driver.find_element_by_xpath('//*[@id="platform-order-id"]').send_keys(order)

#选择货币
ele = driver.find_element_by_xpath("//select[@class='input-xsmall  input-inline form-control']")
s = Select(ele)
s.select_by_visible_text('AED')
time.sleep(0.5)

#选择物流方式
ele = driver.find_element_by_xpath("//select[@name='order.logisticsType']")
s = Select(ele)
s.select_by_visible_text('4PX物流-新加坡挂号')
time.sleep(0.5)

#选择日期
driver.find_element_by_xpath("//input[@name='order.paidDate']").click()
driver.switch_to_frame(0)
driver.find_element_by_xpath('//*[@id="dpOkInput"]').click()
driver.switch_to.default_content()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#选择商品
SKU='ZLY4082502A'
driver.find_element_by_xpath('//*[@id="item-sku-0"]').send_keys(SKU)
driver.find_element_by_xpath("//input[@name='order.orderItems[0].saleQuantity']").send_keys('1')
driver.find_element_by_xpath("//input[@name='order.orderItems[0].productPrice']").send_keys('23')


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#收件信息
driver.find_element_by_xpath('//input[@name="order.buyerName"]').send_keys('许寿龙')

buyerId=random.randint(100000,1000000)
driver.find_element_by_xpath('//input[@name="order.buyerId"]').send_keys(buyerId)
driver.find_element_by_xpath('//input[@name="order.buyerEmail"]').send_keys('ynin2gjs6tr@thrubay.com')

Province=random.choice(['Kansas','Florida','Texas','Illinois','California'])
driver.find_element_by_xpath('//input[@name="order.buyerStateOrProvince"]').send_keys(Province)
# 555 Lexington Avenue, 10th Floor, Room 202  91776
#     90230
#   91723
#     91740
#   92647
street=random.choice(['555 Lexington Avenue, 10th Floor, Room 202','4114 Sepulveda Blvd',
        '137 W San Bernardino Rd','1959 Auto Center Dr','16701 Beach Blvd.'])

driver.find_element_by_xpath('//input[@name="order.street"]').send_keys(street)

Code=random.choice(['91776','90230','91723','91740','92647'])
driver.find_element_by_xpath('//input[@name="order.buyerPostalCode"]').send_keys(Code)


driver.find_element_by_xpath('//input[@name="order.buyerTel"]').send_keys('285-3600')
# driver.find_element_by_xpath('//input[@name="order.buyerMobile"]').send_keys(xx)

City=random.choice(['Gardena','Alhambra','Glendora','Temecula','Exeter'])
driver.find_element_by_xpath('//input[@name="order.buyerCity"]').send_keys(City)
ele = driver.find_element_by_xpath('//select[@name="order.buyerCountryCode"]')
s = Select(ele)
s.select_by_visible_text('United States(美国US)')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="fixed-bottom"]/div/button').click()


WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="orderIds"]')))
driver_get=driver.find_element_by_xpath('//input[@name="orderIds"]')
s=driver_get.get_attribute('value')
print('按货打单：{0}'.format(s))