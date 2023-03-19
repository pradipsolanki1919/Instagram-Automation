from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class TestData():

    # chrome executable path
    # ser = Service("C:\\chromedriver.exe")
    # CHROME_EXECUTABLE_PATH = webdriver.Chrome(ChromeDriverManager().install())

    # Basic variable
    BASE_URL = "https://www.instagram.com/"
    USER_NAME = "Use your username here"
    PASSWORD = "Use your password here"

    # important titles
    LOGIN_PAGE_TITLE = "Instagram"
    HOME_PAGE_TITLE = "Instagram"




