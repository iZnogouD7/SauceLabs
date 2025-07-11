import time

from Locators.alllocators import LoginPageLocators
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def login(self,username,password):
        self.type_in_element(LoginPageLocators.username_field,username)
        self.type_in_element(LoginPageLocators.password_field,password)
        self.click_element(LoginPageLocators.login_button)
        print("Logged in successfully")
        time.sleep(3)

    def get_error_message(self):
        return self.get_text_from_element(LoginPageLocators.error_field_path)

    def get_url(self):
        return self.driver.current_url

    def  get_title(self):
        return self.driver.title

    def are_elements_displayed(self):
        return (self.is_displayed(LoginPageLocators.username_field) and
                self.is_displayed(LoginPageLocators.password_field) and
                self.is_displayed(LoginPageLocators.login_button))
    