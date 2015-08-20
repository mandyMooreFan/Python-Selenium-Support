from webDriverSupport import *

google = wd('http://www.google.com',"NONE")
google.open()

support(google,'//*[@id="lst-ib"]').xpath_send_keys("idkmybffmark.com")
support(google,'//*[@id="sblsbb"]/button').xpath_click()