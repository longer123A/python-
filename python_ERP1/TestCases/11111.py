#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from python_ERP.PageObjects.stock_kucun_page import PutStor
from python_ERP.PageLocators.suggest_jianyi import SuPusing as loc
import pytest
from python_ERP.Common import logger
import logging
import time
from python_ERP.PageObjects.kucun import KuCun
from python_ERP.PageObjects.suggest_jianyi_page import GetOrdervalue
from python_ERP.PageObjects.list_caiguo_page import ListPu
from python_ERP.PageObjects.rku_scan import Scan
import random
from python_ERP.PageObjects.my_sql import MySql
from python_ERP.PageObjects.ng_pending_page_cli import NgPending
@pytest.mark.usefixtures("login_web")

# 采购前的库存：kucun
#采购的数量：size
@pytest.mark.put
class TestPutStorage:

    @pytest.mark.month
    #月结标签
    def test_new_order_month(self, login_web):
        logging.info("*********入库：开始执行月结入库用例*********")
        number= random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  #库存管理方法
        GetOrder=GetOrdervalue(login_web)#采购页面方法，包含BasePage
        listp=ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        #点击库存管理按钮
        PutSto.click_stocon()
        #点击建议采购按钮
        PutSto.click_suging()
        #增加筛选订单条件
        GetOrder.filtrate_order('月结')
        #获取订单SKU
        sku=GetOrder.get_order_sku()
        #获取订单采购数量
        size=int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        #获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        #输入SKU搜索
        GetOrder.input_sku(sku)
        #勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        #alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku,number)

        time.sleep(2)
        #~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number,size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei=KuCun(login_web).get_kucun(sku)
        assert int(int(kucun)+int(size))==int(kucun_gei)

    @pytest.mark.half
    # 半月结标签
    def test_new_order_half(self, login_web):
        logging.info("*********入库：开始执行半月结入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('半月结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.week
    # 周结标签
    def test_new_order_week(self, login_web):
        logging.info("*********入库：开始执行周结入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('周结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.offline
    # 线下现结标签
    def test_new_order_offline(self, login_web):
        logging.info("*********入库：开始执行线下现结入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('线下现结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.wire
    # 电汇标签
    def test_new_order_wire(self, login_web):
        logging.info("*********入库：开始执行电汇入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('电汇')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.pay
    # 款到发货标签
    def test_new_order_pay(self, login_web):
        logging.info("*********入库：开始执行款到发货入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('款到发货')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.transnational
    #跨境宝支付标签
    def test_new_order_transnational(self, login_web):
        logging.info("*********入库：开始执行跨境宝支付入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('跨境宝支付')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.ax
    # 阿里账期标签ax标记
    def test_new_order_Alibaba(self, login_web):
        logging.info("*********入库：开始执行阿里账期入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('阿里账期')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.ax
    # 线上现结标签ax标记
    def test_new_order_offline(self, login_web):
        logging.info("*********入库：开始执行线上现结入库用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('线上现结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # t=MySql().get_sku(sku)
        # qr=t+'.'+sku
        # login_web.switch_to.default_content()
        sca.qc_to_scan(sku)
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(int(kucun) + int(size)) == int(kucun_gei)

















   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NG：输入不通过原因  NG采购待处理~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 月结,pass
    def test_order_ng_month(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)
        ng=NgPending(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('月结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        #不通过修改
        sca.qc_ng_scan(sku)
        ng.get_pending(sku,'pass')

        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)



    # ~~~~~~~~~~~~~~~~~~NG：尺寸不符  NG采购待处理~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 半月结'pass'
    def test_order_ng_half(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('半月结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # 不通过修改
        sca.qc_ng_scan(sku,'尺寸')
        ng.get_pending(sku, 'pass')
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NG：颜色不符  NG采购待处理~~~~~~~~~~~~~~~

    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 周结,
    def test_order_ng_week(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('周结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # 不通过修改
        sca.qc_ng_scan(sku,'颜色')
        ng.get_pending(sku, 'pass')
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NG：款式不符  NG采购待处理~~~~~~~~~~~~~~~
    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 线下现结
    def test_order_ng_offline(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('线下现结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # 不通过修改
        sca.qc_ng_scan(sku,'款式')
        ng.get_pending(sku, 'pass')
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~NG入库待处理~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NG：输入不通过原因 NG入库待处理~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 月结,
    def test_order_ng_month(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)
        ng=NgPending(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('月结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        #不通过修改
        sca.qc_ng_scan(sku,statu='ssss')
        ng.get_pending(sku, 'pass')

        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)



    # ~~~~~~~~~~~~~~~~~~NG：尺寸不符 NG入库待处理~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 半月结
    def test_order_ng_half(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('半月结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # 不通过修改
        sca.qc_ng_scan(sku,'尺寸',statu='ssss')
        ng.get_pending(sku, 'pass')
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NG：颜色不符  NG入库待处理~~~~~~~~~~~~~~~

    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 周结,
    def test_order_ng_week(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('周结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # 不通过修改
        sca.qc_ng_scan(sku,'颜色',statu='ssss')
        ng.get_pending(sku, 'pass')
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NG：款式不符  NG入库待处理~~~~~~~~~~~~~~~
    @pytest.mark.ng
    # [月结,半月结,周结,线下现结,电汇,款到发货,跨境宝支付,阿里账期,线上现结]
    # NG 输入不通过原因  NG采购待处理
    # 线下现结
    def test_order_ng_offline(self, login_web):
        logging.info("*********入库：开始执行输入不通过原因，NG采购待处理用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        sca = Scan(login_web)

        time.sleep(4)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order('线下现结')
        # 获取订单SKU
        sku = GetOrder.get_order_sku()
        # 获取订单采购数量
        size = int(GetOrder.get_order_size())
        logging.info('采购的数量为{0}'.format(size))
        time.sleep(1)
        # 获取库存
        kucun = KuCun(login_web).get_kucun(sku)
        logging.info("库存为：{0}".format(kucun))
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 输入SKU搜索
        GetOrder.input_sku(sku)
        # 勾选订单并且生成采购订单
        time.sleep(3)
        GetOrder.choose_order()
        time.sleep(3)
        # alert弹窗处理
        GetOrder.get_alert()
        time.sleep(3)
        # ~~~~~~~~~~~~~~采购单列表
        # listp.input_SUK(sku)
        listp.bulk_operation(sku, number)

        time.sleep(2)
        # ~~~~~~~~~扫描区~~~~~~~~~~~~
        sca.back_to_scan(number)
        sca.ex_to_scan(number, size)
        # 不通过修改
        sca.qc_ng_scan(sku,'款式',statu='ssss')
        ng.get_pending(sku, 'pass')
        # sca.rku_to_scan(qr)
        time.sleep(1)
        kucun_gei = KuCun(login_web).get_kucun(sku)
        assert int(kucun) == int(kucun_gei)
