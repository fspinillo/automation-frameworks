# -*- coding: utf-8 -*-
"""
Page class serves as a central point to write helper methods for the 
selenium base.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):

    def __init__(self, driver):
        self.driver = driver
    
    def wait_to_click(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
        finally:
            self.driver.find_element(*locator).click()