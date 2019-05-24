from python_ERP.PageObjects.login_page import LoginPage
from python_ERP.PageObjects.home_page import HomePage
from python_ERP.PageObjects.order_guanli_page import OrderPage
import pytest
from python_ERP.PageObjects.xinjian_page import NewPage
from python_ERP.Common import logger
import logging
import time
from python_ERP.PageObjects.kdi_page import KdiLeavePage
from python_ERP.PageObjects.kdi_scan import KdiScan
from python_ERP.PageObjects.wuliu_receive import Wuliu
from python_ERP.Common.do_excel import DoExcel
from python_ERP.Common.dir_config import *
from python_ERP.PageObjects.yunshu_pipei import YunPipei
from python_ERP.TestDatas.chuh_scan_data import *
from python_ERP.PageObjects.stock_kucun_page import PutStor
from python_ERP.PageObjects.kucun import KuCun
from python_ERP.PageObjects.suggest_jianyi_page import GetOrdervalue
from python_ERP.PageObjects.list_caiguo_page import ListPu
from python_ERP.PageObjects.rku_scan import Scan
import random
from python_ERP.PageObjects.ng_caig_rku_cli import NgPending
from python_ERP.PageObjects.qc_noorder_bulp_ddai import NoGoodPage
@pytest.mark.usefixtures("login_web")

@pytest.mark.qx
class TestPermisVa:

    @pytest.mark.qxanh
    def test_permisva_anh(self,login_web):
        logging.info("*********权限：开始执行平台账号权限验证用例*********")
        hoen = HomePage(login_web)
        # 新建订单按钮页面操作
        ord = OrderPage(login_web)
        # 新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        yunshu =YunPipei(login_web)
        login = LoginPage(login_web)
        hoen.click_to_merge()
        ord.new_order()

        #打单方式
        mold = "按货打单"
        code = new.new_order_qx('AliExpress',mold)
        #第一行第二列为平台订单号
        DoExcel(testcases_dir, 'AliExpress').write_back(1,2,code)
        login.clear_login()
        #~~~~~~~~~~~~~~~切换员工账号~~~~~~~~~~~~~
        use_yg = DoExcel(testcases_dir,'AliExpress').do_excel('yuangong',1,1)
        login.login(use_yg['yuangong'])
        time.sleep(2)
        #查询订单号并且移动至待合并状态
        ord.jian_move_he_qx(code)
        #~~~~~~~~~~~~~~切换经理账号~~~~~~~~~~~~~~~
        login.clear_login()
        use_jli = DoExcel(testcases_dir, 'AliExpress').do_excel('jingli', 2, 1)
        login.login(use_jli['jingli'])
        time.sleep(2)
        #待合并
        ord.chaxun_code(code)
        #获取运输方式
        get_moth_index=ord.freight_gu("权限")
        time.sleep(1)

        #修改运输方式和添加跟踪号
        dingdan_code = ord.xiu_kdi_moth_qx(wuli_data[get_moth_index], code)
        # #查找运输方式
        yunshu_genre=yunshu.get_yunshu(wuli_data[get_moth_index])
        ord.chaxun_code(code)
        # #待合并---等待打单
        yunshu_mold=move.qx_hb_move_daidadan(yunshu_genre)
        # #判断仓库
        cangku=move.get_cangku()
        login.clear_login()
        if cangku == "塘厦仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 6, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
        elif cangku == "大浪仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 7, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
        elif cangku == "石岩仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 8, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)

        ord.chaxun_code(code)
        #等待打单——打单
        move.qx_dengdai_move_dadan(yunshu_mold,mold)
        # ~~~~~~~~~~~~~~切换仓库主管账号~~~~~~~~~~~~~~~

        #搜索订单
        ord.chaxun_code(code)
        #获取订单状态
        order_status=move.get_status()
        if "核对打单" in order_status:
            hedui_sku =move.get_sku_qx()
            scan_mold =move.get_scan_mold()
            kd_snac.qx_scan(dingdan_code, hedui_sku, scan_mold)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_index], code)
            ord.chaxun_code(code)
            assert '已发货' in move.get_status()
        else:
            #锁定订单
            sku=move.dadna_move_suo_qx(code,order_status)
            #扫描，SKU还未保存
            #获取扫描方式（注意：核对扫描不存在锁单操作）
            ord.chaxun_code(code)
            scan_mold = move.get_scan_mold()
            kd_snac.qx_scan(dingdan_code,sku,scan_mold)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_index], code)
            ord.chaxun_code(code)
            assert '已发货' in move.get_status()

    @pytest.mark.qxak
    def test_permisva_ank(self, login_web):
        logging.info("*********权限：开始执行平台账号权限验证用例*********")
        hoen = HomePage(login_web)
        # 新建订单按钮页面操作
        ord = OrderPage(login_web)
        # 新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        yunshu = YunPipei(login_web)
        login = LoginPage(login_web)
        hoen.click_to_merge()
        ord.new_order()

        # 打单方式
        mold = "按框打单"
        code = new.new_order_qx('AliExpress', mold)
        # 第一行第二列为平台订单号
        DoExcel(testcases_dir, 'AliExpress').write_back(1, 2, code)

        login.clear_login()
        # ~~~~~~~~~~~~~~~切换员工账号~~~~~~~~~~~~~
        use_yg = DoExcel(testcases_dir, 'AliExpress').do_excel('yuangong', 1, 1)
        login.login(use_yg['yuangong'])
        time.sleep(2)
        # 查询订单号并且移动至待合并状态
        ord.jian_move_he_qx(code)
        # ~~~~~~~~~~~~~~切换经理账号~~~~~~~~~~~~~~~
        login.clear_login()
        use_jli = DoExcel(testcases_dir, 'AliExpress').do_excel('jingli', 2, 1)
        login.login(use_jli['jingli'])
        time.sleep(2)
        # 待合并
        ord.chaxun_code(code)
        # 获取运输方式
        get_moth_index = ord.freight_gu("权限")
        time.sleep(1)

        # 修改运输方式和添加跟踪号
        dingdan_code = ord.xiu_kdi_moth_qx(wuli_data[get_moth_index], code)
        # #查找运输方式
        yunshu_genre = yunshu.get_yunshu(wuli_data[get_moth_index])
        ord.chaxun_code(code)
        # #待合并---等待打单
        yunshu_mold = move.qx_hb_move_daidadan(yunshu_genre)
        # #判断仓库
        cangku = move.get_cangku()
        login.clear_login()
        if cangku == "塘厦仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 6, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
        elif cangku == "大浪仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 7, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
        elif cangku == "石岩仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 8, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)

        ord.chaxun_code(code)
        # 等待打单——打单
        move.qx_dengdai_move_dadan(yunshu_mold, mold)
        # ~~~~~~~~~~~~~~切换仓库主管账号~~~~~~~~~~~~~~~

        # 搜索订单
        ord.chaxun_code(code)
        # 获取订单状态
        order_status = move.get_status()
        if "核对打单" in order_status:
            hedui_sku = move.get_sku_qx()
            scan_mold = move.get_scan_mold()
            kd_snac.qx_scan(dingdan_code, hedui_sku, scan_mold)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_index], code)
            ord.chaxun_code(code)
            assert '已发货' in move.get_status()
        else:
            # 锁定订单
            sku = move.dadna_move_suo_qx(code, order_status)
            # 扫描，SKU还未保存
            ord.chaxun_code(code)
            # 获取扫描方式（注意：核对扫描不存在锁单操作）
            scan_mold = move.get_scan_mold()
            kd_snac.qx_scan(dingdan_code, sku, scan_mold)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_index], code)
            ord.chaxun_code(code)
            assert '已发货' in move.get_status()

    @pytest.mark.qxduop
    def test_permisva_duop(self, login_web):
        logging.info("*********权限：开始执行平台账号权限验证用例*********")
        hoen = HomePage(login_web)
        # 新建订单按钮页面操作
        ord = OrderPage(login_web)
        # 新建订单页面操作
        new = NewPage(login_web)
        move = KdiLeavePage(login_web)
        kd_snac = KdiScan(login_web)
        wuli = Wuliu(login_web)
        yunshu = YunPipei(login_web)
        login = LoginPage(login_web)
        hoen.click_to_merge()
        ord.new_order()

        # 打单方式
        mold = "多品打单"
        code = new.new_order_qx('AliExpress', mold)
        # 第一行第二列为平台订单号
        DoExcel(testcases_dir, 'AliExpress').write_back(1, 2, code)
        login.clear_login()
        # ~~~~~~~~~~~~~~~切换员工账号~~~~~~~~~~~~~
        use_yg = DoExcel(testcases_dir, 'AliExpress').do_excel('yuangong', 1, 1)
        login.login(use_yg['yuangong'])
        time.sleep(2)
        # 查询订单号并且移动至待合并状态
        ord.jian_move_he_qx(code)
        # ~~~~~~~~~~~~~~切换经理账号~~~~~~~~~~~~~~~
        login.clear_login()
        use_jli = DoExcel(testcases_dir, 'AliExpress').do_excel('jingli', 2, 1)
        login.login(use_jli['jingli'])
        time.sleep(2)
        # 待合并
        ord.chaxun_code(code)
        # 获取运输方式
        get_moth_index = ord.freight_gu("权限")
        time.sleep(1)

        # 修改运输方式和添加跟踪号
        dingdan_code = ord.xiu_kdi_moth_qx(wuli_data[get_moth_index], code)
        # #查找运输方式
        yunshu_genre = yunshu.get_yunshu(wuli_data[get_moth_index])
        ord.chaxun_code(code)
        # #待合并---等待打单
        yunshu_mold = move.qx_hb_move_daidadan(yunshu_genre)
        # #判断仓库
        cangku = move.get_cangku()
        login.clear_login()
        if cangku == "塘厦仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 6, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
        elif cangku == "大浪仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 7, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
        elif cangku == "石岩仓库":
            use_zhuguan = DoExcel(testcases_dir, 'AliExpress').do_excel('zhuguan', 8, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)

        ord.chaxun_code(code)
        # 等待打单——打单
        move.qx_dengdai_move_dadan(yunshu_mold, mold)
        # ~~~~~~~~~~~~~~切换仓库主管账号~~~~~~~~~~~~~~~

        # 搜索订单
        ord.chaxun_code(code)
        # 获取订单状态
        order_status = move.get_status()
        if "核对打单" in order_status:
            hedui_sku = move.get_sku_qx()
            scan_mold = move.get_scan_mold()
            kd_snac.qx_scan(dingdan_code, hedui_sku, scan_mold)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_index], code)
            ord.chaxun_code(code)
            assert '已发货' in move.get_status()
        else:
            # 锁定订单
            sku = move.dadna_move_suo_qx(code, order_status)
            # 扫描，SKU还未保存
            ord.chaxun_code(code)
            # 获取扫描方式（注意：核对扫描不存在锁单操作）
            scan_mold = move.get_scan_mold()
            kd_snac.qx_scan(dingdan_code, sku, scan_mold)
            kd_snac.kdi_scan_cku(wuli_data[get_moth_index], code)
            ord.chaxun_code(code)
            assert '已发货' in move.get_status()

    @pytest.mark.qxrku
    @pytest.mark.qxrku_ok
    def test_permisva_rku_qx(self, login_web):
        logging.info("*********入库：开始执行周结入库权限的用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        login = LoginPage(login_web)
        sca = Scan(login_web)
        login.clear_login()
        use_zhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('zhuguan', 1, 1)
        login.login(use_zhuguan['zhuguan'])
        time.sleep(2)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order_qx()
        # 获取订单SKU
        try:
            sku = GetOrder.get_order_sku()
        except:
            assert GetOrder.get_no_text() == '没有记录'
        else:
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
            listp.bulk_operation(sku, number)


            time.sleep(2)
            login.clear_login()
            use_huihscan = DoExcel(testcases_dir, 'qxrku').do_excel('huihscan', 2, 1)
            login.login(use_huihscan['huihscan'])
            time.sleep(2)
            # # # ~~~~~~~~~扫描区~~~~~~~~~~~~
            sca.back_to_scan(number)
            time.sleep(2)
            login.clear_login()
            use_kdiscan = DoExcel(testcases_dir, 'qxrku').do_excel('kdiscan', 3, 1)
            login.login(use_kdiscan['kdiscan'])
            time.sleep(2)
            sca.ex_to_scan(number, size)
            time.sleep(1)
            login.clear_login()
            use_qcscan = DoExcel(testcases_dir, 'qxrku').do_excel('qcscan', 4, 1)
            login.login(use_qcscan['qcscan'])
            time.sleep(2)

            input_qr_code=sca.qc_to_scan_qx(sku)
            # 扫描结束
            time.sleep(1)
            login.clear_login()
            use_rkscan = DoExcel(testcases_dir, 'qxrku').do_excel('rkscan', 5, 1)
            login.login(use_rkscan['rkscan'])
            time.sleep(2)
            sca.rku_to_scan(input_qr_code)
            time.sleep(1)
            login.clear_login()
            use_zhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('zhuguan', 1, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
            kucun_gei = KuCun(login_web).get_kucun(sku)
            assert int(int(kucun) + int(size)) == int(kucun_gei)

    @pytest.mark.qxrku
    @pytest.mark.qxrku_caigou_pass
    def test_permisva_rku_xshou_pass_qx(self, login_web):
        logging.info("*********入库：开始执行周结入库权限的用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        login = LoginPage(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)
        qcno = NoGoodPage(login_web)
        login.clear_login()
        use_zhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('zhuguan', 1, 1)
        login.login(use_zhuguan['zhuguan'])
        time.sleep(2)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order_qx()
        # 获取订单SKU
        try:
            sku = GetOrder.get_order_sku()
        except:
            assert GetOrder.get_no_text() == '没有记录'
        else:
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
            listp.bulk_operation(sku, number)
            xuhao = listp.get_xuhao()
            time.sleep(2)
            login.clear_login()
            use_huihscan = DoExcel(testcases_dir, 'qxrku').do_excel('huihscan', 2, 1)
            login.login(use_huihscan['huihscan'])
            time.sleep(2)
            # # # ~~~~~~~~~扫描区~~~~~~~~~~~~
            sca.back_to_scan(number)
            time.sleep(2)
            login.clear_login()
            use_kdiscan = DoExcel(testcases_dir, 'qxrku').do_excel('kdiscan', 3, 1)
            login.login(use_kdiscan['kdiscan'])
            time.sleep(2)
            sca.ex_to_scan(number, size)
            time.sleep(1)
            login.clear_login()
            use_qcscan = DoExcel(testcases_dir, 'qxrku').do_excel('qcscan', 4, 1)
            login.login(use_qcscan['qcscan'])
            time.sleep(2)
            sca.qc_ng_scan(sku, '款式')
            #~~~~~~~~~~~~~~~~~~切换账号~~~~~~~~~~~~~~~~~~~
            login.clear_login()
            use_ckuzhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('ckuzhuguan', 6, 1)
            login.login(use_ckuzhuguan['ckuzhuguan'])
            time.sleep(2)
            ng.get_pending(sku, 'pass')
            time.sleep(1)
            qcno.wait_dispose(sku, xuhao)
            assert qcno.wait_order() == '等待QC'
            kucun_gei = KuCun(login_web).get_kucun(sku)
            assert int(kucun) == int(kucun_gei)

    @pytest.mark.qxrku
    @pytest.mark.qxrku_caigou_ng
    def test_permisva_rku_xshou_ng_qx(self, login_web):
        logging.info("*********入库：开始执行周结入库权限的用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        login = LoginPage(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)
        qcno = NoGoodPage(login_web)
        login.clear_login()
        use_zhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('zhuguan', 1, 1)
        login.login(use_zhuguan['zhuguan'])
        time.sleep(2)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order_qx()
        # 获取订单SKU
        try:
            sku = GetOrder.get_order_sku()
        except:
            assert GetOrder.get_no_text() == '没有记录'
        else:
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
            listp.bulk_operation(sku, number)
            xuhao = listp.get_xuhao()
            time.sleep(2)
            login.clear_login()
            use_huihscan = DoExcel(testcases_dir, 'qxrku').do_excel('huihscan', 2, 1)
            login.login(use_huihscan['huihscan'])
            time.sleep(2)
            # # # ~~~~~~~~~扫描区~~~~~~~~~~~~
            sca.back_to_scan(number)
            time.sleep(2)
            login.clear_login()
            use_kdiscan = DoExcel(testcases_dir, 'qxrku').do_excel('kdiscan', 3, 1)
            login.login(use_kdiscan['kdiscan'])
            time.sleep(2)
            sca.ex_to_scan(number, size)
            time.sleep(1)
            login.clear_login()
            use_qcscan = DoExcel(testcases_dir, 'qxrku').do_excel('qcscan', 4, 1)
            login.login(use_qcscan['qcscan'])
            time.sleep(2)
            sca.qc_ng_scan(sku, '颜色')
            # ~~~~~~~~~~~~~~~~~~切换账号~~~~~~~~~~~~~~~~~~~
            login.clear_login()
            use_zhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('zhuguan', 1, 1)
            login.login(use_zhuguan['zhuguan'])
            time.sleep(2)
            ng.get_pending(sku, 'ng')
            time.sleep(1)

            qcno.nogood_dispose(sku, xuhao)
            assert qcno.get_order() == 'QC不良品'
            kucun_gei = KuCun(login_web).get_kucun(sku)
            assert int(kucun) == int(kucun_gei)

    @pytest.mark.qxrku
    @pytest.mark.qxrku_ng
    def test_permisva_rku_ng_qx(self, login_web):
        logging.info("*********入库：开始执行周结入库权限的用例*********")
        number = random.randint(100000, 1000000)
        PutSto = PutStor(login_web)  # 库存管理方法
        GetOrder = GetOrdervalue(login_web)  # 采购页面方法，包含BasePage
        listp = ListPu(login_web)
        login = LoginPage(login_web)
        sca = Scan(login_web)
        ng = NgPending(login_web)
        qcno = NoGoodPage(login_web)
        login.clear_login()
        use_zhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('zhuguan', 1, 1)
        login.login(use_zhuguan['zhuguan'])
        time.sleep(2)
        # 点击库存管理按钮
        PutSto.click_stocon()
        # 点击建议采购按钮
        PutSto.click_suging()
        # 增加筛选订单条件
        GetOrder.filtrate_order_qx()
        # 获取订单SKU
        try:
            sku = GetOrder.get_order_sku()
        except:
            assert GetOrder.get_no_text() == '没有记录'
        else:
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
            listp.bulk_operation(sku, number)
            xuhao = listp.get_xuhao()
            time.sleep(2)
            login.clear_login()
            use_huihscan = DoExcel(testcases_dir, 'qxrku').do_excel('huihscan', 2, 1)
            login.login(use_huihscan['huihscan'])
            time.sleep(2)
            # # # ~~~~~~~~~扫描区~~~~~~~~~~~~
            sca.back_to_scan(number)
            time.sleep(2)
            login.clear_login()
            use_kdiscan = DoExcel(testcases_dir, 'qxrku').do_excel('kdiscan', 3, 1)
            login.login(use_kdiscan['kdiscan'])
            time.sleep(2)
            sca.ex_to_scan(number, size)
            time.sleep(1)
            login.clear_login()
            use_qcscan = DoExcel(testcases_dir, 'qxrku').do_excel('qcscan', 4, 1)
            login.login(use_qcscan['qcscan'])
            time.sleep(2)
            sca.qc_ng_scan(sku, '颜色',statu='入库待处理')
            # ~~~~~~~~~~~~~~~~~~切换账号~~~~~~~~~~~~~~~~~~~
            login.clear_login()
            use_ckuzhuguan = DoExcel(testcases_dir, 'qxrku').do_excel('ckuzhuguan', 6, 1)
            login.login(use_ckuzhuguan['ckuzhuguan'])
            time.sleep(2)
            ng.get_rku_pending(sku, '废弃')
            time.sleep(1)
            qcno.feiqi_dispose(sku, xuhao)
            assert qcno.get_feiqi() == '已废弃'
            time.sleep(1)
            kucun_gei = KuCun(login_web).get_kucun(sku)
            assert int(kucun) == int(kucun_gei)
