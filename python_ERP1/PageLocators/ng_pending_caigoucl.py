

from selenium.webdriver.common.by import By

class NgPending:
    #收发货管理
    receive_dispatch = (By.XPATH,'//*[@id="menu_13000000"]')
    #NG采购待处理
    ng_pending = (By.XPATH,'//*[@id="menu_13121400"]')
    #SKU输入
    sku_input = (By.XPATH,'//*[@id="product-sku"]')
    #搜索按钮
    seek_button = (By.XPATH,'//*[@id="search-form"]//button[1]')

    #第一个订单勾选
    noe_dan = (By.XPATH,'//div[@class="page-container"]//tr[@id][1]//*[@name="inIds"]')
    #NG采购操作栏
    ng_procu = (By.XPATH,'//select[@class="form-control input-medium input-inline  order-do"]')
    #PASS
    pass_che = (By.XPATH,'//select[@class="form-control input-medium input-inline  order-do"]//*[@value="pass"]')
    #PASS-text
    pass_text = (By.XPATH,'//*[@id="pass-reason"]')
    #NG
    ng_che = (By.XPATH,'//select[@class="form-control input-medium input-inline  order-do"]//*[@value="ng"]')
    #NG —text
    ng_text = (By.XPATH,'//table[@class="ui-dialog-grid"]//textarea')
    #处理结果
    result = (By.XPATH,'//*[@id="s2id_ng-reason"]')
    # 结果输入
    result_input = (By.XPATH,'//*[@id="select2-drop"]//*[@class="select2-search"]//input')
    # result_click = (By.XPATH,'//table[@class="ui-dialog-grid"]//a//span[1]')
    #OK按钮
    button_ok =(By.XPATH,'//*[@data-id="ok"]')