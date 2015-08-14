from webDriverSupport import *

google = wd('http://www.google.com',"NONE")
google.open()

searchbar = support(google,'//*[@id="lst-ib"]').xpath_element()
searchbar.send_keys("idkmybffmark.com")
searchbar.submit()

google.driver.quit()