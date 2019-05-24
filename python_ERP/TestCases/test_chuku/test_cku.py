#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
from python_ERP.PageObjects.home_page import HomePage
from python_ERP.PageObjects.order_guanli_page import OrderPage
import pytest
from selenium import webdriver
from python_ERP.PageObjects.xinjian_page import NewPage
from python_ERP.Common import logger
import logging
import time
from python_ERP.PageObjects.kdi_page import KdiLeavePage
from python_ERP.PageObjects.kdi_scan import KdiScan
from python_ERP.PageObjects.wuliu_receive import Wuliu
from python_ERP.Common.BasePage import BasePage
from python_ERP.TestDatas.chuh_scan_data import wuli_data
@pytest.mark.usefixtures("login_web")
@pytest.mark.cku
class TestNewOrder:
    @pytest.mark.anh
    def test_chuku_order_anh(self,login_web):
        logging.info("*********入库：开始执行按货打单（快递）用例*********")
        hoen=HomePage(login_web)
        #新建订单按钮页面操作
        ord=OrderPage(login_web)
        #新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        hoen.click_to_merge()

        ord.new_order()

        code=new.new_order('按货打单')

        #待检查--待合并
        ord.jian_move_he(code)
        get_moth_transportation=ord.freight_gu(moth='快递')
        if get_moth_transportation!="无快递":
            #订单号
            dingdan_code=ord.xiu_kdi_moth(wuli_data[get_moth_transportation],code)
            move.he_move_dengdai(code)
            move.dengdai_move_print(code,'按货打单')
            sku=move.dadna_move_suo(code,'按货打单')

            #~~~~~~~~~~~~~~~~~~~~~~~~~扫描分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            kd_snac.kdi_scan_anh(sku)
            # ~~~~~~~~~~~~~~~~~~~~~~~~~物流分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            order_statu = ord.get_order_statu(dingdan_code)
            if order_statu == "快递-待处理":
                ord.xiugai_money()
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'

            else:
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code)=='等待物流收包'

        else:
            BasePage(login_web)._screenshot(model_name='无快递截图')
            pass

    @pytest.mark.ank
    def test_chuku_order_ank(self,login_web):
        logging.info("*********入库：开始执行按框打单（快递）用例*********")
        hoen=HomePage(login_web)
        #新建订单按钮页面操作
        ord=OrderPage(login_web)
        #新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        hoen.click_to_merge()

        ord.new_order()
        code=new.new_order('按框打单')

        #待检查--待合并
        ord.jian_move_he(code)
        get_moth_transportation=ord.freight_gu(moth='快递')
        if get_moth_transportation!="无快递":
            #sku
            dingdan_code=ord.xiu_kdi_moth(wuli_data[get_moth_transportation],code)
            move.he_move_dengdai(code)
            move.dengdai_move_print(code,'按框打单')
            sku=move.dadna_move_suo(code,'按框打单')

            #~~~~~~~~~~~~~~~~~~~~~~~~~扫描分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            kd_snac.kdi_scan_ank(sku)

            # ~~~~~~~~~~~~~~~~~~~~~~~~~物流分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            order_statu = ord.get_order_statu(dingdan_code)
            if order_statu == "快递-待处理":
                ord.xiugai_money()
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'
            else:
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'
        else:
            BasePage(login_web)._screenshot(model_name='无快递截图')
            pass

    @pytest.mark.duopin
    def test_chuku_order_duopin(self, login_web):
        logging.info("*********入库：开始执行多品打单（快递）用例*********")
        hoen = HomePage(login_web)
        # 新建订单按钮页面操作
        ord = OrderPage(login_web)
        # 新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        hoen.click_to_merge()

        ord.new_order()
        code = new.new_order('多品打单')

        # 待检查--待合并
        ord.jian_move_he(code)
        get_moth_transportation = ord.freight_gu('快递')
        if get_moth_transportation != "无快递":
            # 订单号
            dingdan_code=ord.xiu_kdi_moth(wuli_data[get_moth_transportation], code)
            move.he_move_dengdai(code)
            move.dengdai_move_print(code, '多品打单')
            sku = move.dadna_move_suo(code, '多品打单')

            # ~~~~~~~~~~~~~~~~~~~~~~~~~扫描分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            picihao_code = kd_snac.get_picihao(dingdan_code,'快递-多品打单')
            qr=kd_snac.duopin_scan_kdi(picihao_code,sku)
            kd_snac.duo_scan_hedui(qr)

            #~~~~~~~~~~~~~~~~~~~~~~~~~~扫描分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            order_statu = ord.get_order_statu(dingdan_code)
            if  order_statu=="快递-待处理":
                ord.xiugai_money()
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'
            else:
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(picihao_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'

            # ~~~~~~~~~~~~~~~~~~~~~~~~~物流分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
            BasePage(login_web)._screenshot(model_name='无快递截图')
            pass

    @pytest.mark.hedui
    def test_chuku_order_hedui(self,login_web):
        logging.info("*********入库：开始执行核对打单（快递）用例*********")
        hoen=HomePage(login_web)
        #新建订单按钮页面操作
        ord=OrderPage(login_web)
        #新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        hoen.click_to_merge()

        ord.new_order()
        code=new.new_order('核对打单')

        #待检查--待合并
        ord.jian_move_he(code)
        get_moth_transportation=ord.freight_gu(moth='快递')
        if get_moth_transportation!="无快递":
            #sku
            dingdan_code=ord.xiu_kdi_moth(wuli_data[get_moth_transportation],code)
            move.he_move_dengdai(code)
            move.dengdai_move_print(code,'核对打单')

            # ~~~~~~~~~~~~~~~~~~~~~~~~~扫描分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            kd_snac.hedui_scan(dingdan_code)

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~扫描分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            order_statu = ord.get_order_statu(dingdan_code)
            if order_statu == "快递-待处理":
                ord.xiugai_money()
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'
            else:
                kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
                wuli.wuliu_scna(dingdan_code)
                assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'
            #
            # ~~~~~~~~~~~~~~~~~~~~~~~~~物流分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
            BasePage(login_web)._screenshot(model_name='无快递截图')
            pass


    @pytest.mark.duocang
    #多仓库——多仓打单
    def test_duocang_order(self,login_web):
        logging.info("*********入库：开始执行多仓库—多仓打单用例*********")
        hoen = HomePage(login_web)
        # 新建订单按钮页面操作
        ord = OrderPage(login_web)
        # 新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        hoen.click_to_merge()

        ord.new_order()
        code = new.new_order('多仓打单')
        ord.jian_move_he(code)
        get_moth_transportation = ord.freight_gu(moth='多仓')
        if get_moth_transportation!="无快递":
            #sku
            dingdan_code=ord.xiu_kdi_moth(wuli_data[get_moth_transportation],code)
            move.he_move_dengdai(code)
            move.dengdai_move_duoca(code)
            sku=move.dadna_move_suo_duocang(code)
            picihao_code = kd_snac.get_picihao_cuocang(dingdan_code)
            #~~~~~~~~~~~~~~~~~~~~~扫描阶段~~~~~~~~~~~~
            qr=kd_snac.duopin_scan_duocang(picihao_code,sku)
            kd_snac.hedui_scan_duocang(qr)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_transportation], code)
            # ~~~~~~~~~~~~~~~~~~~~~扫描阶段~~~~~~~~~~~~~
            wuli.wuliu_scna(dingdan_code)
            assert wuli.judge_order_cku(dingdan_code) == '等待物流收包'
        else:
            BasePage(login_web)._screenshot(model_name='无快递截图')
            pass