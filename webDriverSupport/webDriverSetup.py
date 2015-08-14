from selenium import webdriver
import os

class wd:
    def __init__(self,site,browser):
        self.site = site
        self.browser = browser
        self.driver = ""
        self.instance = ""
        #Call the method to set driver
        self.set_driver()

    def set_driver(self):
        path = os.getcwd()
        if self.browser == "CHROME":
            self.driver = webdriver.Chrome(path + "\webDriverSupport\drivers\chromedriver.exe")
        elif self.browser == "IE":
            self.driver = webdriver.Ie(path + "\webDriverSupport\drivers\IEDriverServer.exe")
        else:
            self.driver = webdriver.Firefox()

    def open(self):
        self.driver.get(self.site)