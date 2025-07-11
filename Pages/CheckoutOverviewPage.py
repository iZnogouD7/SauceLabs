from Locators.alllocators import CheckoutOverviewPageLocators, CheckoutPageLocators
from Pages.BasePage import BasePage


class CheckoutOverviewPage(BasePage):
    def click_finish_button(self):
        #self.click_element(CheckoutOverviewPageLocators.finish_button_path)
        self.find_element(CheckoutOverviewPageLocators.finish_button_path).click()

    def click_cancel_button(self):
        self.click_element(CheckoutPageLocators.cancel_button_path)

    def get_checkout_overview_page_url(self):
        return self.driver.current_url
    def get_checkout_overview_page_title(self):
        return self.driver.title