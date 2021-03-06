from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class support:
    def __init__(self,wd,element):
        self.wd = wd.driver
        self.element = element

    def xpath_wait_clickable(self):
        WebDriverWait(self.wd, 30).until(
            EC.element_to_be_clickable((By.XPATH,self.element))
        )

    def xpath_hover(self):
        self.xpath_wait_clickable()
        self.element = self.wd.find_element_by_xpath(self.element)
        hov = ActionChains(self.wd).move_to_element(self.element)
        hov.perform()

    def xpath_element(self):
        self.xpath_wait_clickable()
        return self.wd.find_element_by_xpath(self.element)

    def xpath_click(self):
        self.xpath_wait_clickable()
        self.element = self.wd.find_element_by_xpath(self.element)
        self.element.click()

    def xpath_send_keys(self,text):
        self.text = text
        self.xpath_wait_clickable()
        self.element = self.wd.find_element_by_xpath(self.element)
        self.element.send_keys(text)