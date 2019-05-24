import pytest

pytest.main(["-m","ng1","--html=HtmlTestReport/report.html",
             "--junitxml=HtmlTestReport/report.xml"])