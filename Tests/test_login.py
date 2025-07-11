import pytest
import time
from Locators.alllocators import LoginPageLocators
from Pages.LoginPage import LoginPage
from Utils.FileReader import load_csv_data


@pytest.mark.parametrize("username,password,expected", load_csv_data("Data/login_data.csv"))
def test_login(driver,username, password, expected):
    login_page = LoginPage(driver)
    assert login_page.get_url()== LoginPageLocators.loginpageUrl
    assert login_page.are_elements_displayed()== True
    login_page.login(username, password)
    time.sleep(3)
    if expected=="success":
        assert login_page.get_url() == "https://www.saucedemo.com/inventory.html",f"Wrong url: {login_page.get_url()}"
        assert login_page.get_title()== "Swag Labs",f"Wrong title: {login_page.get_title()}"
    elif expected=="failure":
        assert "Epic sadface" in login_page.get_error_message(),f"Got error message: {login_page.get_error_message()}"
    elif expected=="lockedout":
        assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message(),f"Expected locked user error message: {login_page.get_error_message()}"
    else:
        print("Unexpected value and Error Found")

def test_password_masking(driver):
    login_page = LoginPage(driver)
    assert login_page.get_url()== LoginPageLocators.loginpageUrl
    password_field=login_page.find_element(LoginPageLocators.password_field)
    assert password_field.get_attribute("type") == "password",f"Password should be masked by default. Got attribute:{password_field.get_attribute('type')}"
    login_page.click_element(LoginPageLocators.show_password_path)
    assert password_field.get_attribute("type")=="text","Password should be visible after clicking show password button"

# def test_locked_user_login(driver):
#     login_page = LoginPage(driver)
#     login_page.login(LoginPageLocators.locked_username,LoginPageLocators.valid_password)
#     error_message=login_page.get_error_message()
#     assert "Epic sadface: Sorry, this user has been locked out." in error_message,f"Expected locked user error message: {error_message}"
