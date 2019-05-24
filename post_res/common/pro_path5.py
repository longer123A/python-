import os

poject_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
                         #顶层目录

test_data_path=os.path.join(poject_path,'test_data','test.xlsx')
                         #测试数据目录

test_result_html=os.path.join(poject_path,'test_result','html','test_report.html')
                         #html测试报告目录

test_result_log=os.path.join(poject_path,'test_result','log','log.txt')
                         #log日志输出
