from webDriverSupport import *

google = wd('http://www.google.com',"NONE").open()
support(google,"//*[@value = 'Google Search']").xpath_click()