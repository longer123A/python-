import logging
from post_res.common.pro_path5 import *

fh=logging.FileHandler(test_result_log,encoding='UTF-8')
                        #日志打印至txt文件
sh=logging.StreamHandler()
                        #日志打印至控制台
formatter='%(asctime)s-%(levelname)s-%(filename)s-日志信息：%(message)s'
                  #asctime当前时间
                  #levelnme文本形式的日志级别
                  #filename调用日志输出函数的模块的文件名
                  #nameLogger的名字，默认为ROOT
                  #用户输出的消息

dfmt='%d, %b, %Y, %H:%M:%S'
                  #日期格式
                  #年月日时分秒

logging.basicConfig(level=logging.ERROR,handlers=[fh,sh],format=formatter,datefmt=dfmt)
                  #基础配置，你需要打印的最低级别日志
                  #fh,sh分别是打印至txt文件和控制台