import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

""" This class is parent page of all the pages"""
""" it contains all the generic and utilities for all the pages"""

class BasePage():

    """Constructor method"""
    def __init__(self, driver):
        self.driver = driver

    """Actions"""

    """This is going click on element"""
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    """This is used for send keys"""
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).send_keys(text)

    """This is used to get the text of the element"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return element.text

    """This is verify that element is visible"""
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    """This is verify the title of the element"""
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title









