#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
import pytest
from selenium import webdriver
from python_ERP1.PageObjects.login_page import LoginPage
# from PageObjects.index_page import IndexPage
#测试数据
from python_ERP1.TestDatas import  CommonDatas as CD
import logging
import time
#登陆用例的前置 和后置

#setup和teardown
@pytest.fixture
def init_loginEnv():
    #前置
    # 初始化浏览器会话
    logging.info("=====用例前置：初始化浏览器会话:打开谷歌浏览器，访问系统网址：{0}=======".format(CD.web_url))
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_url)
    time.sleep(1)
    loginp = LoginPage()
    yield [driver,loginp]
    #后置
    logging.info("=====用例后置：关闭谷歌浏览器会话=======")
    driver.quit()


#定义一个函数，并在这个函数当中，实现用例的准备工作和清理工作。
# 在函数的前面加上 @pytest.fixture
#fixture可以设置作用域范围
@pytest.fixture
def login_web():
    # 初始化浏览器会话
    logging.info("=====用例前置：初始化浏览器会话，登陆WEB系统=======")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_url)
    LoginPage(driver).login(CD.user, CD.passwd,CD.code)
    #yield 准备工作和清理工作的分限线。上面是准备工作。下面的是清理工作
    #有返回值的情况下，返回值写在yield后面。
    yield driver
    logging.info("=====用例后置：关闭浏览器会话,清理环境=======")
    driver.quit()


#setupClass,teardownClass
@pytest.fixture(scope="class")
def class_demo():
    print("==========我是class级别的fixtures=============")


#测试
@pytest.fixture
def fuction_diff_demo():
    print("==============demo demo demo=================")
