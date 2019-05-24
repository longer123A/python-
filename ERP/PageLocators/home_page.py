#首页页面元素封装

class HomePage:
    #首页点击按钮
    home="//a[text()='首页']"

    #待销售处理方式
    #无法判断邮寄方式
    sell_mail="//div[@id='status-pending']/a[1]"
    #有留言
    sell_leave="//div[@id='status-pending']/a[2]"
    #SKU不存在
    sell_SKU = "//div[@id='status-pending']/a[3]"
    #加转接头
    sell_adapter = "//div[@id='status-pending']/a[4]"
    # 收件人信息不完善
    sell_adre = "//div[@id='status-pending']/a[5]"
    # 申报信息不完整
    sell_declare = "//div[@id='status-pending']/a[6]"
    # 申请跟踪号异常
    sell_number = "//div[@id='status-pending']/a[7]"

    pass