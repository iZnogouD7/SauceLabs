import pytest

from Locators.alllocators import LoginPageLocators
from Pages.LoginPage import LoginPage
from Pages.OtherPage import OtherPage


@pytest.fixture()
def open_product_page(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    menu =OtherPage(driver)
    return menu
def test_menu_visibility(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    assert menu.is_menu_sidebar_displayed() == True,"Menu bar not displayed"
def test_menu_cancel(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.click_menu_cancel()
    assert menu.is_menu_sidebar_displayed(),"Menu bar is still displayed"
def test_click_all_item(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.go_to_all_item()
    assert "inventory" in menu.get_current_url()

def test_click_reset_item(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.reset_app_state()
    menu.click_menu_cancel()
    assert True
def test_logout(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.logout()
    assert menu.get_current_url() == LoginPageLocators.loginpageUrl

def test_footer_visibility(open_product_page):
    footer = open_product_page
    assert footer.is_footer_displayed(),"Footer bar not displayed"
def test_footer_twitter(open_product_page):
    footer = open_product_page
    footer.click_twitter_logo()
    assert True
def test_footer_facebook(open_product_page):
    footer = open_product_page
    footer.click_facebook_logo()
    assert True
def test_footer_linkedin(open_product_page):
    footer = open_product_page
    footer.click_linkedin_logo()
    assert True




