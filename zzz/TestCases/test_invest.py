#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/13 15:24

#正常场景
#前置
#1、用户余额够用 ：充值一个亿。
#2、查看有多少余额，然后不够200块，我就去充值。如果有就不充值了。
#不走web页面，走接口来实现。
#有可投资的标

#步骤
# 首页-直接选第一个标；
#标页面 - 获取用户可用余额
# 标页面-输入金额，进行投资。投资金额：200
# 点击投资成功弹出框中的   查看并激活按钮

#验证
# 个人页面：获取用户可用余额
#比对：投资金额  = 投资前的余额 - 投资后的余额
# 投资记录？？？
# 利息是多少？

from TestDatas import invest_data as ID

from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage
import pytest
from Common import logger
import logging

@pytest.mark.invest
@pytest.mark.usefixtures("login_web")
class TestInvest:

    @pytest.mark.smoke
    def test_invest_success(self,login_web):
        logging.info("*********投资用例：正常场景-投资成功*********")
        # 首页 - 选一个标来投资 - 直接选第一个标 - --- / 随机选一个
        IndexPage(login_web).click_first_investButton()
        # 标页面 - 获取投资前的个人余额
        bid_page = BidPage(login_web)
        userMoney_beforeInvest = bid_page.get_user_leftMoney()
        # 标页面 - 输入投资金额 ，点击投标按钮
        bid_page.invest(ID.invest_money)
        # 标页面 - 投资成功弹出框 ，点击查看并激活按钮
        bid_page.click_activeButton_from_investSuccess_popup()
        # #验证
        # 个人页面 - 获取用户当前余额
        userMoney_afterInvest = UserPage(login_web).get_user_leftMoney()
        # 1、余额：投资前获取一下，投资后再获取一下。求差值，如果等于投资金额，那正确。
        assert ID.invest_money == int(float(userMoney_beforeInvest) - float(userMoney_afterInvest))
        # PS：自动化测试独立帐号。
        # 2、个人页面 - 投资记录获取。

    def test_invest_failed_by_No100(self, login_web):
        logging.info("*********投资用例：异常场景：投资金额为非100的整数倍*********")
        # 首页 - 选一个标来投资 - 直接选第一个标 - --- / 随机选一个
        IndexPage(login_web).click_first_investButton()
        # 标页面 - 获取投资前的个人余额
        bid_page = BidPage(login_web)
        userMoney_beforeInvest = bid_page.get_user_leftMoney()
        # 标页面 - 输入投资金额 ，点击投标按钮
        bid_page.invest(ID.no100_data["money"])
        # 获取提示信息
        errorMsg = bid_page.get_errorMsg_from_popup()
        # 刷新
        login_web.refresh()
        # 获取用户余额
        userMoney_afterInvest = bid_page.get_user_leftMoney()
        # 断言
        assert errorMsg == ID.no100_data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest
    #
    # def test_invest_fail_no10(self):
    #     pass

#异常场景  - 用户余额不够 - 手功用例
#异常场景  - 投资》标的可投余额 - 手功用例