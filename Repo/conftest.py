import time
import pytest

from selenium.webdriver import Chrome

@pytest.fixture()
def get_driver_webdriver():
    global driver

    #Change to your local Chrome Driver Directory
    driver = Chrome(executable_path='C:\\chromedriver.exe')
    
    driver.get("https://public:Let$BeC001@bgp-qa.gds-gov.tech")
    driver.maximize_window()       

    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()