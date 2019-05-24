#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/11 21:26

#测试用例 = 页面对象当中的页面功能 + 测试数据
from PageObjects.index_page import IndexPage
#测试数据
from TestDatas import login_datas as LD
from Common import logger
import logging
import pytest

#fixture的函数名称
@pytest.mark.usefixtures("class_demo")
@pytest.mark.usefixtures("init_loginEnv")
class TestLogin:

    #正常场景用例 - 登陆成功
    #init_loginEnv(fixture函数名称)接收 fixture运行的返回值  [driver,loginp]
    def test_login_success(self,init_loginEnv):
        logging.info("*********登陆用例：正常场景：使用正确的用户名和密码登陆*********")
        #步骤 - 登陆：用户名：18684720553  密码：python 比对数据：我的帐户[小小蜂96027]
        init_loginEnv[1].login(LD.login_succs["username"],LD.login_succs["passwd"])
        #断言
        try:
            assert IndexPage(init_loginEnv[0]).get_nickName() == LD.login_succs["check"]
        except AssertionError:
            logging.exception("断言失败")
            raise

    @pytest.mark.parametrize("data",LD.login_noData)
    def test_login_fail_noUser(self,init_loginEnv,data):
        logging.info("*********登陆用例：异常场景：没有用户名/没有密码/用户名格式不正确*********")
        # 步骤 - 登陆：用户名：  密码：python 比对数据：弹出错误提示内容：请输入手机号
        init_loginEnv[1].login(data["username"], data["passwd"])
        # 断言
        try:
            assert init_loginEnv[1].get_errorMsg_fromLoginArea() == data["check"]
        except AssertionError:
            logging.exception("断言失败")
            raise

    @pytest.mark.parametrize("caseData",LD.wrong_data)
    def test_login_wrongLoginInfo(self, init_loginEnv,caseData):
        logging.info("*********登陆用例：异常场景：错误的密码/用户尚未注册*********")
        # 步骤
        init_loginEnv[1].login(caseData["user"], caseData["passwd"])
        # 验证-检查点
        try:
            assert init_loginEnv[1].get_errorMsg_from_pageCenter() == caseData["check"]
        except AssertionError:
            logging.exception("断言失败")
            raise
