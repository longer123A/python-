#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/23 20:42
import unittest

class TestInvest(unittest.TestCase):


    def setUp(self):
        #打开浏览器，登陆前程贷
        self.driver = webdriver.Chrome()
        self.driver.get(web_url)
        LoginPage(self.driver).login(user,passwd)

    def tearDown(self):
        self.driver.quit()