#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/10/16 21:20

#unitest收集测试用例
import pytest

pytest.main(["--html=HtmlTestReport/report.html",
             "--junitxml=HtmlTestReport/report.xml"])