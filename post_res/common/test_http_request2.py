import unittest
from ddt import ddt,data
from post_res.common.my_logger6 import *
from post_res.common.do_excel3 import DoExcel
from post_res.common.http_request1 import HttpRequest


test_data=DoExcel(test_data_path,'Sheet1').do_excel()
          #读取Excel数据
COOKIES={}
@ddt
          #装饰为测试类
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        self.t=DoExcel(test_data_path,'Sheet1')

    @data(*test_data)
          #拆分数据
    def test_api(self,item):
        global TestResult
        global COOKIES   #声明全局变量
        print('正在执行第{0}条用例：{1}'.format(item['CaseId'],item['Tltle']))
        res=HttpRequest().http_request(item['Url'],eval(item['Param']),item['Method'],COOKIES)
                                                  #带参数访问接口
                                                  #res等于响应内容
        if res.cookies!={}:
            COOKIES=res.cookies
        try:
             self.assertEqual(item['Expected'],int(res.json()['code']))
                                                  #根据响应内容的code断言结果
             TestResult='PASS'
        except Exception as e:
             logging.error('断言错误{0}'.format(e))
             TestResult='Fail'
             raise e
        finally:
            self.t.write_back(int(item['CaseId'])+1,7,str(res.json()))
                                                  #Excel只能支持传递字符串
            self.t.write_back(int(item['CaseId'])+1,8,TestResult)