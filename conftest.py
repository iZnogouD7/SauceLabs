import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    BaseUrl = "https://www.saucedemo.com/"
    driver = webdriver.ChromiumEdge()
    driver.maximize_window()
    driver.get(BaseUrl)
    yield driver
    driver.quit()
