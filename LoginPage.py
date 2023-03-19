from selenium.webdriver.common.by import By
from Config.Config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage

class LoginPage(BasePage):

    """ By locator - OR"""

    EMAIL = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//form[@id='loginForm']/div/div[3]")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    FORGOT_PASSWORD = (By.XPATH, "//*[@id='loginForm']/a")
    FACEBOOK_LINK = (By.XPATH, "//form[@id='loginForm']/div/div[5]")
    APPSTORE = (By.CSS_SELECTOR, "img.Rt8TI")
    GooglePlay = (By.XPATH, "//div[@class='iNy2T']/a[2]/img")

    """ Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to check the signup link"""
    def is_signup_link_exits(self):
        return self.is_visible(self.SIGNUP_LINK)

    """this is used to check forgot password link"""
    def is_forgot_password_link_exits(self):
        return self.is_visible(self.FORGOT_PASSWORD)

    """this is used to check facebook link exits or not"""
    def is_facebook_link_exits(self):
        return self.is_visible(self.FACEBOOK_LINK)

    """this method will check that app store link is available or not"""
    def is_appstore_link_exits(self):
        return self.is_visible(self.APPSTORE)

    """this method will check that google play link is available or not"""
    def is_googleplay_link_exits(self):
        return self.is_visible(self.GooglePlay)

    """this is used to do login """
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

