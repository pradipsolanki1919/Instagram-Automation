import pytest
from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

    """Verify that signup link is available"""
    def test_signup_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_signup_link_exits()
        assert flag

    """Verify title is match"""
    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        title = self.loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    """ Verify Email and Password fields are available"""
    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    """Verify forgot password like is available"""
    def test_forgotPassword_link(self):
        self.loginpage = LoginPage(self.driver)
        forgotLink = self.loginpage.is_forgot_password_link_exits()
        return forgotLink

    """Verify that facebook link is exits or not"""
    def test_facebooklink(self):
        self.loginpage = LoginPage(self.driver)
        facebbokLink = self.loginpage.is_facebook_link_exits()
        return facebbokLink

    """Verify that download from App Store link is available"""
    def test_appstore(self):
        self.loginpage = LoginPage(self.driver)
        appstore = self.loginpage.is_appstore_link_exits()
        return appstore

    """Verify that download from Google Play link is available"""
    def test_googleplay(self):
        self.loginpage = LoginPage(self.driver)
        googlplay = self.loginpage.is_googleplay_link_exits()
        return googlplay


