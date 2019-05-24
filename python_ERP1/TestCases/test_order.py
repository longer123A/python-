#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from python_ERP1.PageObjects.home_page import HomePage
from python_ERP1.PageObjects.order_xinjian_page import OrderPage
import pytest
from python_ERP1.Common import logger
import logging
import time
@pytest.mark.usefixtures("login_web")
class TestNewOrder:
    @pytest.mark.smoke
    def test_new_order(self,login_web):
        logging.info("*********新建订单：新建订单开始*********")
        # 首页 -点击待合并按钮
        HomePage(login_web).click_to_merge()

        #切换窗口
        OrderPage(login_web).window_switch_order(-1)

        #点击新建订单按钮
        OrderPage(login_web).new_order()

        #切换至新建订单窗口
        OrderPage(login_web).window_switch_order(-1)

        time.sleep(5)

    # def test_invest_failed_by_No100(self, login_web):
    #     logging.info("*********投资用例：异常场景：投资金额为非100的整数倍*********")
    #     # 首页 - 选一个标来投资 - 直接选第一个标 - --- / 随机选一个
    #     IndexPage(login_web).click_first_investButton()
    #     # 标页面 - 获取投资前的个人余额
    #     bid_page = BidPage(login_web)
    #     userMoney_beforeInvest = bid_page.get_user_leftMoney()
    #     # 标页面 - 输入投资金额 ，点击投标按钮
    #     bid_page.invest(ID.no100_data["money"])
    #     # 获取提示信息
    #     errorMsg = bid_page.get_errorMsg_from_popup()
    #     # 刷新
    #     login_web.refresh()
    #     # 获取用户余额
    #     userMoney_afterInvest = bid_page.get_user_leftMoney()
    #     # 断言
    #     assert errorMsg == ID.no100_data["check"]
    #     assert userMoney_afterInvest == userMoney_beforeInvest
    # #
    # def test_invest_fail_no10(self):
    #     pass

#异常场景  - 用户余额不够 - 手功用例
#异常场景  - 投资》标的可投余额 - 手功用例