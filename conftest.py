import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Config.Config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):

    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.implicitly_wait(10)
        web_driver.maximize_window()
    if request.param == "firefox":
        web_driver = webdriver.Firefox(GeckoDriverManager().install())

    request.cls.driver = web_driver

    yield
    web_driver.quit()