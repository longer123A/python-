#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu

import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"Quanx_data","quanxian_data.xlsx")

htmlreport_dir =  os.path.join(base_dir,"HtmlTestReport")

logs_dir =  os.path.join(base_dir,"Logs")
# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"ScreenShot")
textdata_dir = os.path.join(base_dir,"Textdata","data.txt")
# print(logs_dir)
