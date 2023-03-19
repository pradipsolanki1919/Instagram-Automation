import pytest

from Config.Config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Home(BaseTest):

    """Verify home page title"""
    def test_home_page_title(self):
        self.loginpage = LoginPage(self.driver)
        self.homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homepage.click_on_SaveInformation()
        self.homepage.click_on_NotNowButton()
        self.homepage.click_on_notification()
        title = self.homepage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

        print("Code Run Successfully.")
# American standard code for incharge