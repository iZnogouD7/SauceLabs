from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self,locator):
        try:

            return self.wait.until(EC.presence_of_element_located(locator))
        except:
            raise Exception(f"Timed Out waiting for Element {locator} not found")

    def find_elements(self,locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except:
            raise Exception(f"Timed Out waiting for Elements {locator} not found")

    def click_element(self,locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except:
            raise Exception(f"Failed to click Element {locator} not found")

    def type_in_element(self,locator,text):
        try:
            element=self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except:
            raise Exception(f"Failed to type into element {locator} with text {text} not found")

    def get_text_from_element(self,locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text
        except:
            print(f"Couldn't get text from element {locator}")
            return 0

    def get_count(self,locator):
        return len(self.find_elements(locator))

    def is_displayed(self,locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            print(f"'{locator} is not displayed'")
            return False

    def find_element_by_class_name(self,class_name):
        return self.driver.find_elements(class_name)

    def get_current_url(self):
        return self.driver.current_url
    def switch_to_new_window(self,main_window):
        for window in self.driver.window_handles:
            if window != main_window:
                return window
        raise AssertionError("No new windows found after click")