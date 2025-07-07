from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_in_element(self,locator,text):
        element=self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def get_count(self,locator):
        return len(self.wait.until(EC.presence_of_all_elements_located(locator)))

    def is_displayed(self,locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    def find_element_by_class_name(self,class_name):
        return self.wait.until(EC.find_all_elements(class_name))
