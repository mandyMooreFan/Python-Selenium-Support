from selenium import webdriver
import os

class wd:
    def __init__(self,site,browser,enviroment,directory):
        self.site = site
        self.browser = browser
        self.enviroment = enviroment
        self.directory = directory
        self.driver = ""
        self.instance = ""
        #Call the method to set driver
        self.set_driver()

    def set_driver(self):
        path = os.getcwd()
        if self.browser == "CHROME":
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory" : self.directory}
            chromeOptions.add_experimental_option("prefs",prefs)
            chromedriver = path + "\webDriverSupport\drivers\chromedriver.exe"
            self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        elif self.browser == "IE":
            self.driver = webdriver.Ie(path + "\webDriverSupport\drivers\IEDriverServer.exe")
        else:
            self.driver = webdriver.Firefox()

    def open(self):
        self.driver.get(self.site)