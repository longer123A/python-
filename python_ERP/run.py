import pytest

#入库用例收集seller
# pytest.main(["-m","qxrku",'--reruns','2',"--html=HtmlTestReport/report.html"])
pytest.main(["-m","qxrku_ng","--html=HtmlTestReport/report.html"])
# pytest.main(["-m","qxanh","--html=HtmlTestReport/report.html"])
# pytest.main(["-m","qxanh","--html=HtmlTestReport/report.html"])
# pytest.main(["-m","qxanh","--html=HtmlTestReport/report.html"])
#出库用例收集
# pytest.main(['--reruns','2',"--html=HtmlTestReport/report.html"])