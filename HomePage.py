from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):

    HOME_PAGE_TITLE = (By.XPATH, "//i[@class='sp_jY02qVAhKr8_2x sx_7a4472']")
    PROFILE = (By.XPATH, "//div[@id='f33e27c1c8fbbcc']/div/div")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    SAVE_INFORMATION = (By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button")
    NOTNOW_BUTTON = (By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]")
    NOTIFICATION = (By.CSS_SELECTOR, "button._a9_1")


    """Constructor method"""
    def __init__(self, driver):
        super().__init__(driver)

    """This will give title of the page"""
    def home_page_title(self, title):
        return self.get_title(title)

    """This will check the profile of the page"""
    def is_profile_exits(self):
        return self.is_visible(self.PROFILE)

    """Click on the search field """
    def search_field_exits(self):
        return self.do_click(self.SEARCH_BUTTON)

    def click_on_SaveInformation(self):
        return self.do_click(self.SAVE_INFORMATION)

    def click_on_NotNowButton(self):
        return self.do_click(self.NOTNOW_BUTTON)

    def click_on_notification(self):
        return self.do_click(self.NOTIFICATION)







