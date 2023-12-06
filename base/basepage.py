from allure_commons.types import AttachmentType
import allure
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_value, locator_type):
        """
        method for explicit wait for an element
        """
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, locator_value)))
            return element
        except Exception as e:
            print("Element not found with given locator type:", e)
        return element

    def get_element(self, locator_value, locator_type="xpath"):
        """
        method to get element on the page
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
        except Exception as e:
            print(f"Element not found with given value {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False
        return element

    def click_element(self, locator_value, locator_type="xpath"):
        """
        method to click an element
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
        except Exception as e:
            # print(f"Element cannot be clicked at: {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False

    def send_text(self, text, locator_value, locator_type="xpath"):
        """
        method to write text into the element
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
            element.clear()
            element.send_keys(text)
            print(f"Send text to element with given value {locator_value}")
        except Exception as e:
            print(f"Unable to send text to element with given value {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False

    def is_element_displayed(self, locator_value, locator_type="xpath"):
        """
        method to verify element is displayed or not
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.is_displayed()
            print(f"Displayed Element with given value {locator_value}")
            return True
        except Exception as e:
            print(f"Element with locator value: {locator_value} is not displayed. ", e)
            self.take_screenshot(locator_type)
            return False

    def is_element_enabled(self, locator_value, locator_type="xpath"):
        """
        method to verify element is enabled or not
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.is_enabled()
            return True
        except Exception as e:
            print(f"Element with locator value: {locator_value} is not enabled. ", e)
            self.take_screenshot(locator_type)
            return False

    def take_screenshot(self, text):
        """
        method to take screenshots for allure report
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def get_element_text(self, locator_value, locator_type="xpath"):
        """
        Method for get element text
        """
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
        except Exception as e:
            print(f"Element not found with given value {locator_value}", e)
            self.take_screenshot(locator_type)
            assert False
        return element.text

    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_hidden_element_attribute(self, locator_value, locator_type="xpath", attribute_name=None):
        """
        method to get element on the page
        """
        element = None
        wait = WebDriverWait(self.driver, 10)
        try:
            locator_type = locator_type.lower()
            element = self.driver.find_element_by_xpath(locator_value)
            attribute_value = element.get_attribute(attribute_name)
        except Exception as e:
            print(f"Element not found with given value {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False
        return attribute_value
