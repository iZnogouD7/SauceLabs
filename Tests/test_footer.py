import pytest
import time

from Locators.alllocators import LoginPageLocators
from Pages.LoginPage import LoginPage
from Pages.OtherPage import OtherPage


def test_footer(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username,LoginPageLocators.valid_password)
    footer_page=OtherPage(driver)
    assert footer_page.is_footer_displayed(), "Footer bar not displayed"

    main_window=driver.current_window_handle

    footer_page.click_twitter_logo()
    time.sleep(2)
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            break
    assert "x.com/saucelabs" in driver.current_url, f"Twitter site is not displayed,Got url:{driver.current_url}"
    driver.close()
    driver.switch_to.window(main_window)
    footer_page.click_facebook_logo()
    assert "facebook.com" in driver.current_url(), f"Facebook site is not displayed, Got url:{driver.current_url}"
    driver.close()
    driver.switch_to.window(main_window)
    footer_page.click_linkedin_logo()
    assert "linkedin.com" in driver.current_url(), f"Linkedin site is not displayed,Got url:{driver.current_url()}"

