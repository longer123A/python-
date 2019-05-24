__author__ = 'xu'
# Time : 2019/5/13 9:07
#主程序入口

import unittest
import HTMLTestRunnerNew
from post_res.common.pro_path5 import *
from post_res.common.test_Eme7 import sendEmail
from post_res.common.test_http_request2 import TestHttpRequest


suite=unittest.TestSuite()
#ddt   加载用例 loader
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


#生成测试报告

with open(test_result_html,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,
                                            title='主题',
                                            description='描述',
                                            tester='许寿龙')
    runner.run(suite)


#添加邮件发送
sendEmail().sen_email('2314799266@qq.com',test_result_html)



