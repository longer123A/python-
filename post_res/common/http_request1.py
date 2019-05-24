import requests
from post_res.common.my_logger6 import *
class   HttpRequest:

    def http_request(self,url,param,method,cookies):
        if method.upper()=='GET':
            try:
                response=requests.get(url,param,cookies=cookies)
            except Exception as e:
                logging.error('get请求错误{0}'.format(e))
                raise e
        else:
            try:
                response=requests.post(url,param,cookies=cookies)

            except Exception as e:
                logging.error('post请求错误{0}'.format(e))
                raise e
        return response